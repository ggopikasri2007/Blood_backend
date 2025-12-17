# from pydantic import BaseModel
# class DonorCreate(BaseModel):
#     donor_id:int 
#     name:str 
#     phone_number:str 
#     address:str 
#     blood_group:str 
#     age:int

from pydantic import BaseModel

class DonorCreate(BaseModel):
    name: str
    phone_number: str
    address: str
    blood_group: str
    age: int
