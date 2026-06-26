from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.resume import Resume

import fitz
import os
import json

from dotenv import load_dotenv
from google.genai import Client

load_dotenv()

client = Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume Analysis"]
)


@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Please upload PDF resume only"
        )

    try:

        pdf_bytes = await file.read()

        doc = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        resume_text = ""

        for page in doc:
            resume_text += page.get_text()

        prompt = f"""
You are an Expert Resume Reviewer and Career Mentor.

Analyze the following resume.

Resume:

{resume_text}

Return ONLY valid JSON.

{{
    "resume_score": 0,
    "skills_found": [],
    "missing_skills": [],
    "strengths": [],
    "improvements": [],
    "career_recommendation": "",
    "placement_readiness": ""
}}

Rules:
- Resume score should be 0-100
- Identify technical skills
- Identify missing skills
- Give career recommendation
- Give placement readiness percentage
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        result = response.text.strip()

        result = result.replace(
            "```json",
            ""
        )

        result = result.replace(
            "```",
            ""
        )

        result = result.strip()

        try:

            analysis = json.loads(result)

        except Exception:

            return {
                "success": False,
                "message": "Gemini returned invalid JSON",
                "raw_response": result
            }

        resume = Resume(
            filename=file.filename,
            resume_score=analysis.get(
                "resume_score",
                0
            ),
            skills_found=json.dumps(
                analysis.get(
                    "skills_found",
                    []
                )
            ),
            missing_skills=json.dumps(
                analysis.get(
                    "missing_skills",
                    []
                )
            ),
            strengths=json.dumps(
                analysis.get(
                    "strengths",
                    []
                )
            ),
            improvements=json.dumps(
                analysis.get(
                    "improvements",
                    []
                )
            ),
            career_recommendation=analysis.get(
                "career_recommendation",
                ""
            ),
            placement_readiness=analysis.get(
                "placement_readiness",
                ""
            )
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        return {
            "success": True,
            "resume_id": resume.id,
            "filename": file.filename,
            "analysis": analysis
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )