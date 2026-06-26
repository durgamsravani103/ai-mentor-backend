\# AI Mentor Backend



\## Overview



AI Mentor is an AI-powered placement preparation platform that helps students analyze resumes, generate AI-based career roadmaps, conduct mock interviews, and interact with an AI chatbot.



\---



\## Features



\- Resume Analysis

\- AI Career Roadmap Generation

\- AI Mock Interview Questions

\- AI Chat Assistant

\- Dashboard Analytics

\- SQLite Database Integration

\- FastAPI REST APIs



\---



\## Tech Stack



\- Python

\- FastAPI

\- SQLAlchemy

\- SQLite

\- Gemini AI

\- PyMuPDF

\- Uvicorn



\---



\## Installation



```bash

git clone https://github.com/durgamsravani103/ai-mentor-backend.git



cd ai-mentor-backend



pip install -r requirements.txt



uvicorn app.main:app --reload

```



\---



\## API Endpoints



\### Resume



POST /api/resume/upload



\### Chat



POST /api/chat/message



\### Roadmap



POST /api/roadmap/generate



\### Mock Interview



POST /api/interview/interview/generate



\### Dashboard



GET /api/dashboard/{user\_id}



\---



\## Database



SQLite



\---



\## AI Model



Gemini 2.5 Flash



\---



\## Author



Sravani

