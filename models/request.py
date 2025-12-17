from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base
from datetime import datetime

class Request(Base):
    __tablename__ = "requests"

    request_id = Column(Integer, primary_key=True, index=True)
    donor_name = Column(String, nullable=False)   # 👈 added
    blood_group = Column(String, nullable=False)
    city = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    message = Column(String, nullable=True)
    request_date = Column(DateTime, default=datetime.utcnow)
