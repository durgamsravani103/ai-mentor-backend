from pydantic import BaseModel
from typing import List


class InterviewQuestionResponse(BaseModel):
    id: int
    question: str


class InterviewQuestionsResponse(BaseModel):
    questions: List[InterviewQuestionResponse]


class InterviewAnswerRequest(BaseModel):
    question: str
    answer: str


class InterviewEvaluationResponse(BaseModel):
    score: int
    feedback: str
    strengths: List[str]
    improvements: List[str]