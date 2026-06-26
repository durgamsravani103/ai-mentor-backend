from fastapi import FastAPI

from app.database import Base, engine

from app.api.auth import router as auth_router
from app.api.onboarding import router as onboarding_router
from app.api.chat import router as chat_router
from app.api.roadmap import router as roadmap_router
from app.api.dashboard import router as dashboard_router
from app.api.interview import router as interview_router
from app.api.resume import router as resume_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Mentor",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI Mentor Backend Running Successfully 🚀"
    }

# Authentication
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

# Onboarding
app.include_router(
    onboarding_router,
    prefix="/api/onboarding",
    tags=["Onboarding"]
)

# AI Chat
app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["AI Chat"]
)

# Resume Analysis
app.include_router(
    resume_router,
    prefix="/api/resume",
    tags=["Resume Analysis"]
)

# Mock Interview
app.include_router(
    interview_router,
    prefix="/api/interview",
    tags=["Mock Interview"]
)

# Roadmap
app.include_router(
    roadmap_router,
    prefix="/api/roadmap",
    tags=["Roadmap"]
)

# Dashboard
app.include_router(
    dashboard_router,
    prefix="/api/dashboard",
    tags=["Dashboard"]
)