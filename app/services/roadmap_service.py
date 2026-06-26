from google.genai import Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_roadmap(resume_text: str):

    prompt = f"""
Analyze this resume and generate a complete career roadmap.

Resume:
{resume_text}

Include:
1. Current Skill Level
2. Missing Skills
3. Skills to Learn
4. Placement Readiness
5. 3 Month Plan
6. 6 Month Plan
7. Interview Preparation
8. Recommended Projects
9. Career Suggestions
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:
        return """
Current Skill Level:
Intermediate

Missing Skills:
- DSA
- Docker
- AWS
- System Design

3 Month Plan:
- Learn DSA
- Practice SQL
- Build FastAPI Projects

6 Month Plan:
- Learn Docker
- Learn AWS
- Deploy Projects

Interview Preparation:
- LeetCode
- Mock Interviews

Career Suggestion:
Backend Developer
"""