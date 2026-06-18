from fastapi import FastAPI
from app.api.prescription import router as prescription_router

app = FastAPI()

app.include_router(
    prescription_router,
    prefix="/prescription",
    tags=["Prescription"]
)

@app.get("/")
def home():
    return {
        "message": "Prescription Analyzer Backend Running"
    }