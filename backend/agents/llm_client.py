
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"  # replace with real endpoint

GEMINI_API_KEY=os.getenv("API_KEY")

def query_gemini(prompt: str, max_tokens=300):
    payload = {
        "prompt": prompt,
        "max_tokens": max_tokens
    }
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        return f"Error: {response.status_code} {response.text}"
