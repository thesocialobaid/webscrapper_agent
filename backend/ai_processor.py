import google.generativeai as genai
from backend.models import DeeplearningCourseList  # Adjust if needed
import os
import json
from dotenv import load_dotenv
load_dotenv()
# Set up your Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create the Gemini model instance (without tools)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def process_with_gemini(html: str, instructions: str) -> str:
    if not html.strip():
        return "Error: No HTML content provided."

    prompt = f"""
You are a highly accurate web content extraction AI.

Given a user's instructions and some raw HTML, extract structured, meaningful, and clean content.

User Instructions:
{instructions.strip()}

---

HTML Content:
{html[:10000]}  # Truncate to first 10,000 chars to avoid token limit issues
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip() if hasattr(response, 'text') else "Error: No valid response from Gemini."
    except Exception as e:
        return f"Error: Gemini processing failed due to {str(e)}"
