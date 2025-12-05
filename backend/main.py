from fastapi import FastAPI
from backend.routes import chat, doctor
from backend.database import engine, Base, SessionLocal
from backend.services.doctor_service import seed_doctors

# Initialize DB Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Healthcare Chatbot API")

# Seed Data on Startup
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    seed_doctors(db)
    db.close()

# Register Routes
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(doctor.router, prefix="/doctors", tags=["Doctors"])
# app.include_router(patient.router, prefix="/patients", tags=["Patients"])

@app.get("/")
def read_root():
    return {"message": "Healthcare Chatbot API is running"}