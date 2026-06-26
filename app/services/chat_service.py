from dotenv import load_dotenv
from google.genai import Client
import os

load_dotenv()

client = Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def generate_response(message: str):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message
        )

        return response.text

    except Exception as e:
        return f"AI Service Busy: {str(e)}"