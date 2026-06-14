from fastapi import APIRouter
from app.schemas.onboarding import OnboardingRequest

router = APIRouter()

@router.post("/")
def save_onboarding(data: OnboardingRequest):
    return {
        "message": "Onboarding Saved Successfully",
        "full_name": data.full_name,
        "college": data.college,
        "degree": data.degree,
        "branch": data.branch,
        "year": data.year,
        "cgpa": data.cgpa,
        "skills": data.skills,
        "target_role": data.target_role
    }