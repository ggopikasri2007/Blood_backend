# from sqlalchemy import Column,Integer,String
# from db.database import Base
# class BloodBank(Base):
#     __tablename__="blood_bank"
#     blood_bank_id=Column(Integer,primary_key=True)
#     name=Column(String)
#     address=Column(String)
#     contact_number=Column(String)
#     image=Column(String)
#     city=Column(String)
#     email=Column(String)


from sqlalchemy import Column, Integer, String
from db.database import Base

class BloodBank(Base):
    __tablename__ = "blood_bank"
    blood_bank_id = Column(Integer, primary_key=True, index=True)  # added index=True for faster lookups
    name = Column(String, nullable=False)
    address = Column(String, nullable=True)
    contact_number = Column(String, nullable=True)
    image = Column(String, nullable=True)
    city = Column(String, nullable=True)
    email = Column(String, nullable=True)

