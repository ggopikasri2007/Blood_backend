from pydantic import BaseModel

class RequestCreate(BaseModel):
    donor_name: str
    blood_group: str
    city: str
    contact_number: str
    message: str | None = None

class RequestUpdate(BaseModel):
    donor_name: str
    blood_group: str
    city: str
    contact_number: str
    message: str | None = None
