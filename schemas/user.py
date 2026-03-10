from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    age: int
    blood_group: str
    city: str
    phone: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    user_id: int
    full_name: str
    email: EmailStr
    age: int
    blood_group: str
    city: str
    phone: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    full_name: str
    email: EmailStr
    age: int
    city: str
    phone: str

    class Config:
        orm_mode = True