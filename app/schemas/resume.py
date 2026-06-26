from pydantic import BaseModel
from typing import List


class RoadmapItem(BaseModel):
    week: int
    goal: str


class ResumeAnalysisResponse(BaseModel):
    filename: str
    resume_score: int
    skills_found: List[str]
    missing_skills: List[str]
    strengths: List[str]
    improvements: List[str]
    career_recommendation: str
    placement_readiness: str
    learning_roadmap: List[RoadmapItem]