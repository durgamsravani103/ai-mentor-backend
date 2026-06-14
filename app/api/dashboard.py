from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_dashboard():

    return {
        "user_name": "Durgam Sravani",
        "target_role": "Python Full Stack Developer",
        "roadmap_progress": 25,
        "completed_tasks": 5,
        "pending_tasks": 15,
        "mock_interviews_completed": 0,
        "resume_score": 0
    }