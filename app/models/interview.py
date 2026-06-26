from sqlalchemy import Column, Integer, Text
from app.database import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    interview_score = Column(Integer)

    feedback = Column(Text)

    strengths = Column(Text)

    improvements = Column(Text)