from google.genai import Client
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_interview_questions(resume_text: str):

    prompt = f"""
You are a senior technical interviewer.

Read this resume carefully.

Resume:
{resume_text}

Generate 10 interview questions based on:

1. Skills
2. Projects
3. Technologies
4. Experience

Return ONLY JSON.

{{
  "questions": [
    {{
      "id": 1,
      "question": ""
    }}
  ]
}}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        result = response.text.strip()

        if result.startswith("```json"):
            result = result.replace("```json", "")
            result = result.replace("```", "")
            result = result.strip()

        return json.loads(result)

    except Exception as e:

        return {
            "success": False,
            "message": f"AI Service Busy: {str(e)}",
            "questions": []
        }