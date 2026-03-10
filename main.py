from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from db.database import Base, engine 
# from routers.donors import donors_router
from routers.blood_bank import blood_bank_router
# from routers.donate import donate_router
from routers.request import request_router
from routers.auth import auth_router   
from routers.donation import donation_router



Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blood_bank_router)
# app.include_router(donors_router)
# app.include_router(donate_router) 
app.include_router(request_router)
app.include_router(auth_router)  
app.include_router(donation_router)
@app.get("/")
def home():
    return {"message": "donors list"}