import fitz
import json
from app.ai.gemini_client import model


async def analyze_resume(file):
    try:
        # Read uploaded PDF
        pdf_content = await file.read()

        # Open PDF
        pdf = fitz.open(
            stream=pdf_content,
            filetype="pdf"
        )

        # Extract text
        resume_text = ""

        for page in pdf:
            resume_text += page.get_text()

        if not resume_text.strip():
            return {
                "success": False,
                "message": "Could not extract text from resume."
            }

        # Gemini Prompt
        prompt = f"""
You are an expert Resume Reviewer and Career Mentor.

Analyze the following resume.

Resume Content:
{resume_text}

Return ONLY valid JSON in this format:

{{
    "resume_score": 0,
    "skills_found": [],
    "missing_skills": [],
    "strengths": [],
    "weaknesses": [],
    "career_recommendation": "",
    "learning_roadmap": []
}}

Rules:
- Resume score must be between 0 and 100.
- Identify technical and soft skills.
- Suggest missing skills.
- Give career recommendation.
- Generate a learning roadmap.
"""

        # Call Gemini
        response = model.generate_content(prompt)

        result = response.text.strip()

        # Remove markdown if Gemini returns ```json
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

        try:
            parsed_result = json.loads(result)

            return {
                "success": True,
                "filename": file.filename,
                "analysis": parsed_result
            }

        except json.JSONDecodeError:
            return {
                "success": True,
                "filename": file.filename,
                "analysis": result
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }