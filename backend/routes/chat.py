from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.services.emergency_service import check_medical_emergency
from backend.services.doctor_service import search_doctors
from backend.database import get_db
from backend.services.llm_service import get_ai_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    language: str = "English"

@router.post("/")
@router.post("/")
async def chat_endpoint(request: ChatRequest, db: Session = Depends(get_db)):
    # 1. Get Smart Response
    ai_reply = get_ai_response(request.message)
    print(f"Debug ai reply:{ai_reply}")

    # 2. Extract Keywords to find Doctors
    recommended_doctors = []
    reply_lower = ai_reply.lower()
    
    # NOTE: We now search for Departments (Cardiology, Dermatology)
    # So we map the AI's "Cardiologist" to the CSV's "Cardio"
    
    search_term = None
    
    if "cardio" in reply_lower or "heart" in reply_lower:
        search_term = "Cardio" # Matches "Cardiology"
    elif "derm" in reply_lower or "skin" in reply_lower:
        search_term = "Dermatolog" # Matches "Dermatology"
    elif "pediatric" in reply_lower or "child" in reply_lower:
        search_term = "Pediatric"
    elif "physician" in reply_lower or "general" in reply_lower:
        search_term = "General"
        
    if search_term:
        recommended_doctors = search_doctors(db, search_term)
        print(f"Dubug doctor found:{len(recommended_doctors)}")

    return {
        "response": ai_reply,
        "recommended_doctors": recommended_doctors
    }