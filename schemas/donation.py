from pydantic import BaseModel
from datetime import datetime

class DonationResponse(BaseModel):
    id: int
    user_id: int
    donation_date: datetime

    class Config:
        orm_mode = True