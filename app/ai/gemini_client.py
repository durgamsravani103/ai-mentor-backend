from dotenv import load_dotenv
from pathlib import Path
from google.genai import Client
import os

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

client = Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello"
)

print(response.text)