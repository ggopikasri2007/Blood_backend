from fastapi import FastAPI 
from db.database import Base, engine 
from routers.donors import  donors_router
from routers.blood_bank import blood_bank_router
from routers.donate import donate_router
from routers.request import request_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(blood_bank_router)
app.include_router(donors_router)
app.include_router(donate_router) 
app.include_router(request_router)

@app.get("/")
def home():
    return {"message": "donors list"}
