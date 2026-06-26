from pydantic import BaseModel
from typing import List


class DashboardResponse(BaseModel):
    resume_score: int
    skills_found: List[str]
    missing_skills: List[str]

    interview_score: int

    roadmap_progress: int

    completed_tasks: int

    pending_tasks: int

    placement_readiness: str

    career_recommendation: str