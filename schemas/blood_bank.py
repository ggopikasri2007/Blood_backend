from pydantic import BaseModel

class BloodBankCreate(BaseModel):
    name: str
    address: str
    contact_number: str
    image: str
    city: str
    email: str

class BloodBankUpdate(BaseModel):
    name: str
    address: str
    city: str
    contact_number: str
    email: str
