from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.prescription import router as prescription_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
