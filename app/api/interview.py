from fastapi import APIRouter

router = APIRouter()

@router.get("/questions")
def get_questions():
    return {
        "questions": [
            {
                "id": 1,
                "question": "What is Python?"
            },
            {
                "id": 2,
                "question": "What is OOP?"
            },
            {
                "id": 3,
                "question": "What is FastAPI?"
            },
            {
                "id": 4,
                "question": "Difference between List and Tuple?"
            },
            {
                "id": 5,
                "question": "What is REST API?"
            }
        ]
    }