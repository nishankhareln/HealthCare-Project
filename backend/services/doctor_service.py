import pandas as pd
from sqlalchemy.orm import Session
from backend.models.doctor import DoctorDB
import os

def seed_doctors(db: Session):
    # Check if DB is already full
    if db.query(DoctorDB).first():
        print("✅ Database already contains data.")
        return
    
    csv_path = os.path.join("data", "doctors.csv")
    
    if os.path.exists(csv_path):
        print(f"📂 Found CSV at: {csv_path}")
        try:
            df = pd.read_csv(csv_path).fillna("")
            print(f"📊 CSV has {len(df)} rows.")
            
            for _, row in df.iterrows():
                print(f"   -> Adding Doctor: {row['name']} ({row['department']})")
                doctor = DoctorDB(
                    hospital=row['hospital'],
                    name=row['name'],
                    department=row['department'],
                    position=row['position'],
                    profile_url=row['profile_url']
                )
                db.add(doctor)
            db.commit()
            print("✅ Data seeded successfully!")
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
    else:
        print(f"❌ CSV file not found at: {csv_path}")

def search_doctors(db: Session, query: str = None):
    """Search by Department (e.g., Cardiology)"""
    if query:
        return db.query(DoctorDB).filter(
            DoctorDB.department.ilike(f"%{query}%")
        ).all()
    return db.query(DoctorDB).all()