import os
import re
import json
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def analyze_prescription_image(image_path):

    image = Image.open(image_path)

    prompt= """
Analyze this prescription image.

Return ONLY valid JSON.

{
    "disease": "",
    "medicines": [],
    "precautions": [],
    "remedies": [],
    "diet": [],
    "emergency": false,
    "emergency reason": "",
    "recommendation": ""
}

Set emergency=true ONLY if the prescription, diagnosis, or medicines suggest a potentially urgent or life-threatening condition requiring prompt medical attention.

Do not mark common illnesses such as:
- Viral fever
- Malaria
- Common infections
- Gastritis
- Routine medications

as emergencies unless there is clear evidence.
"""

    response = model.generate_content(
        [prompt, image]
    )

#     result = response.text.strip()

#     if result.startswith("```json"):
#         result = result.replace("```json", "", 1)

#     if result.endswith("```"):
#         result = result[:-3]

#     result = result.strip()

#     return json.loads(result)

    result = response.text.strip()

    match = re.search(
        r"\{.*\}",
        result,
        re.DOTALL
    )

    if not match:
        raise Exception(
            "Gemini did not return JSON"
        )

    json_text = match.group()

    return json.loads(json_text)