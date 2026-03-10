from pydantic import BaseModel
from datetime import datetime

class RequestCreate(BaseModel):
    patient_name: str | None = None
    blood_group: str
    city: str
    units_needed: int = 1

class RequestUpdate(BaseModel):
    units_received: int
    status: str  # optional: you can validate allowed values ["Pending","Accepted","Completed"]

class RequestResponse(BaseModel):
    request_id: int
    patient_name: str | None
    blood_group: str
    city: str
    units_needed: int
    units_received: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True