from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.interview_service import generate_interview_questions
import fitz

router = APIRouter(
    prefix="/interview",
    tags=["Mock Interview"]
)

@router.post("/generate")
async def generate_questions(
    file: UploadFile = File(...)
):
    try:

        if not file.filename.endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Upload PDF Resume"
            )

        pdf_bytes = await file.read()

        doc = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        resume_text = ""

        for page in doc:
            resume_text += page.get_text()

        questions = generate_interview_questions(
            resume_text
        )

        return questions

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )