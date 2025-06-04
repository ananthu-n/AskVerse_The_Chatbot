# backend/models.py
from sqlalchemy import Column, Integer, String, Enum
from backend.database import Base  # ✅ This should work now
import enum

class RoleEnum(enum.Enum):
    student = "student"
    teacher = "teacher"
    employee = "employee"
    other = "other"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    field_of_interest = Column(String(100), nullable=True)
    role = Column(Enum(RoleEnum), nullable=False)
