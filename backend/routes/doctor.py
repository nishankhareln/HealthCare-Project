from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend.services.doctor_service import search_doctors
from backend.models.doctor import Doctor

router = APIRouter()

@router.get("/", response_model=List[Doctor])
def get_doctors(specialty: str = None, db: Session = Depends(get_db)):
    return search_doctors(db, specialty)