import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_prescription(text):

    prompt = f"""
You are a medical prescription analyzer.

Analyze the prescription text and return ONLY valid JSON.

Prescription Text:
{text}

Return format:

{{
    "disease": "",
    "medicines": [],
    "precautions": [],
    "remedies": [],
    "diet": [],
    "emergency": false
}}
"""
    response = model.generate_content(prompt)

    result = response.text

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    return json.loads(result)