from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    resume_score = Column(Integer)

    skills_found = Column(Text)

    missing_skills = Column(Text)

    strengths = Column(Text)

    improvements = Column(Text)

    career_recommendation = Column(Text)

    placement_readiness = Column(String)