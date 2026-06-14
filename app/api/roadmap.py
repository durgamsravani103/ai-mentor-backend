from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_roadmap():
    return {
        "success": True,
        "message": "Roadmap Retrieved Successfully",
        "roadmap": {
            "Month 1": [
                "Learn Python Basics",
                "Practice Python Programs"
            ],
            "Month 2": [
                "Learn OOP Concepts",
                "Build Mini Python Projects"
            ],
            "Month 3": [
                "Learn SQL",
                "Learn PostgreSQL"
            ],
            "Month 4": [
                "Learn FastAPI",
                "Build REST APIs"
            ],
            "Month 5": [
                "Learn HTML",
                "Learn CSS",
                "Learn JavaScript"
            ],
            "Month 6": [
                "Learn React",
                "Build Frontend Projects"
            ],
            "Month 7": [
                "Build Full Stack Projects",
                "Deploy Applications"
            ],
            "Month 8": [
                "Practice DSA",
                "Solve LeetCode Problems"
            ],
            "Month 9": [
                "Mock Interviews",
                "Resume Preparation"
            ]
        }
    }


@router.post("/generate")
def generate_roadmap():
    roadmap = {
        "Month 1": [
            "Python Basics",
            "Variables",
            "Loops",
            "Functions"
        ],
        "Month 2": [
            "OOP Concepts",
            "Classes",
            "Inheritance",
            "Polymorphism"
        ],
        "Month 3": [
            "SQL",
            "Database Design",
            "PostgreSQL"
        ],
        "Month 4": [
            "FastAPI",
            "REST APIs",
            "JWT Authentication"
        ],
        "Month 5": [
            "HTML",
            "CSS",
            "JavaScript"
        ],
        "Month 6": [
            "React Basics",
            "React Hooks",
            "API Integration"
        ],
        "Month 7": [
            "Full Stack Project",
            "Git & GitHub"
        ],
        "Month 8": [
            "DSA Preparation",
            "Arrays",
            "Strings",
            "Linked Lists"
        ],
        "Month 9": [
            "Mock Interviews",
            "Resume Building",
            "Placement Preparation"
        ]
    }

    return {
        "success": True,
        "message": "Roadmap Generated Successfully",
        "roadmap": roadmap
    }