from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from db.database import Base  

class Donation(Base):
    __tablename__ = "donation"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    donation_date = Column(DateTime, default=datetime.utcnow)

  
    user = relationship("User", back_populates="donations")