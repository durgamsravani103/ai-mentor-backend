from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
def analyze_resume():

    return {
        "resume_score": 75,
        "strengths": [
            "Good Python Skills",
            "FastAPI Knowledge",
            "Projects Available"
        ],
        "improvements": [
            "Add More Projects",
            "Improve DSA",
            "Add Certifications"
        ]
    }