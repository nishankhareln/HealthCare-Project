from turtle import position
from sqlalchemy import Column, Integer, String, Boolean
from backend.database import Base
from pydantic import BaseModel
from typing import Optional

# SQLAlchemy Model (DB Table)
class DoctorDB(Base):
    __tablename__ = "doctors"
    id = Column(Integer,primary_key=True,index=True)
    hospital = Column(String)
    name = Column(String, index=True)
    department = Column(String)
    position = Column(String)
    profile_url= Column(String)




#pydantic model
class Doctor(BaseModel):
    id:int
    name:str
    department:str
    position:str
    profile_url:str

    class Config:
        from_attribute = True


        