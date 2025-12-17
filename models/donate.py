from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.database import Base
from datetime import datetime

class Donate(Base):
    __tablename__ = "donations"

    donation_id = Column(Integer, primary_key=True, index=True)
    donor_id = Column(Integer, ForeignKey("donors.donor_id"), nullable=False)
    full_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    blood_group = Column(String, nullable=False)
    city = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    donation_date = Column(DateTime, default=datetime.utcnow)

    donor = relationship("Donor", backref="donations")

