from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    resume_summary = Column(Text)

    missing_skills = Column(Text)

    roadmap_content = Column(Text)

    progress_percentage = Column(Integer, default=0)

    completed_tasks = Column(Integer, default=0)

    pending_tasks = Column(Integer, default=0)