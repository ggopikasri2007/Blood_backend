from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    blood_group = Column(String(5), nullable=False)
    city = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    donations = relationship("Donation", back_populates="user", cascade="all, delete-orphan")   