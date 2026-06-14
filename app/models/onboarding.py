from sqlalchemy import Column, Integer, String
from app.database import Base

class Onboarding(Base):
    __tablename__ = "onboarding"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)

    target_role = Column(String)
    skill_level = Column(String)
    weak_areas = Column(String)
    daily_study_hours = Column(Integer)
    placement_timeline = Column(String)