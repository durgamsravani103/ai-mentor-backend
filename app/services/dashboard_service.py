from app.database import SessionLocal
from app.models.resume import Resume
import json


def get_dashboard_data(user_id: int):

    db = SessionLocal()

    try:

        latest_resume = (
            db.query(Resume)
            .order_by(Resume.id.desc())
            .first()
        )

        if not latest_resume:
            return {
                "message": "No Resume Found"
            }

        resume_score = latest_resume.resume_score

        placement_readiness = (
            latest_resume.placement_readiness
        )

        overall_ai_score = (
            resume_score +
            int(placement_readiness.replace("%", ""))
        ) // 2

        return {
            "user_id": user_id,

            "resume_score":
                resume_score,

            "placement_readiness":
                placement_readiness,

            "overall_ai_score":
                overall_ai_score,

            "skills_found":
                json.loads(
                    latest_resume.skills_found
                ),

            "missing_skills":
                json.loads(
                    latest_resume.missing_skills
                ),

            "strengths":
                json.loads(
                    latest_resume.strengths
                ),

            "improvements":
                json.loads(
                    latest_resume.improvements
                ),

            "career_recommendation":
                latest_resume.career_recommendation
        }

    finally:
        db.close()