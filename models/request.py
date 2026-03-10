from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base
from datetime import datetime

class Request(Base):
    __tablename__ = "request"

    request_id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(100), nullable=True)
    blood_group = Column(String(5), nullable=False)
    city = Column(String(100), nullable=False)
    units_needed = Column(Integer, nullable=False, default=1)
    units_received = Column(Integer, default=0)
    status = Column(String(20), default="Pending")  # simplified from Enum
    created_at = Column(DateTime, default=datetime.utcnow)