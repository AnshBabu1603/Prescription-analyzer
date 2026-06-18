from fastapi import APIRouter, UploadFile, File
from app.services.prescription_analyzer import (
    analyze_prescription_image
)
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"

@router.get("/test")
def test_route():
    return {
        "status": "Prescription API Working"
    }

@router.post("/upload")
async def upload_prescription(
    file: UploadFile = File(...)
):
    
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    analysis = analyze_prescription_image(
        file_path
    )
    if os.path.exists(file_path):
        os.remove(file_path)

    return {
        "message": "File uploaded successfully",
        "analysis": analysis
    }