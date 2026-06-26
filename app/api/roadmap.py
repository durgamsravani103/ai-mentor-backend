from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.roadmap import Roadmap
from app.services.roadmap_service import generate_roadmap
import fitz

router = APIRouter()


@router.post("/generate")
async def create_roadmap(file: UploadFile = File(...)):

    try:

        pdf_bytes = await file.read()

        doc = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        resume_text = ""

        for page in doc:
            resume_text += page.get_text()

        roadmap_text = generate_roadmap(resume_text)

        db = SessionLocal()

        roadmap_db = Roadmap(
            filename=file.filename,
            resume_summary=resume_text[:1000],
            roadmap_content=roadmap_text
        )

        db.add(roadmap_db)
        db.commit()
        db.refresh(roadmap_db)

        db.close()

        return {
            "roadmap_id": roadmap_db.id,
            "filename": file.filename,
            "roadmap": roadmap_text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )