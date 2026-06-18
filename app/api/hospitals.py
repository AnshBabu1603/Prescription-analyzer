from fastapi import APIRouter
from app.services.hospital_service import get_nearby_hospitals

router = APIRouter()

@router.get("/nearby")
def nearby_hospitals(
    lat: float,
    lng: float
):
    return get_nearby_hospitals(
        lat,
        lng
    )