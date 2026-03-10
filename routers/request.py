from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from models.request import Request
from schemas.request import RequestCreate, RequestUpdate, RequestResponse
from dependencies import get_db

# ✅ Router object
request_router = APIRouter(prefix="/request", tags=["Request"])

# 🔹 Create a new patient request
@request_router.post("/", response_model=RequestResponse)
def create_request(request: RequestCreate, db: Session = Depends(get_db)):
    new_request = Request(
        patient_name=request.patient_name,
        blood_group=request.blood_group,
        city=request.city,
        units_needed=request.units_needed
    )
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

# 🔹 Get all requests
@request_router.get("/", response_model=list[RequestResponse])
def get_requests(db: Session = Depends(get_db)):
    return db.query(Request).all()

# 🔹 Get a specific request by ID
@request_router.get("/{request_id}", response_model=RequestResponse)
def get_request(request_id: int = Path(...), db: Session = Depends(get_db)):
    request = db.query(Request).filter(Request.request_id == request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    return request

# 🔹 Update a request (e.g., units_received or status)
@request_router.put("/{request_id}", response_model=RequestResponse)
def update_request(request_id: int, updated_request: RequestUpdate, db: Session = Depends(get_db)):
    request = db.query(Request).filter(Request.request_id == request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")

    request.units_received = updated_request.units_received
    request.status = updated_request.status

    db.commit()
    db.refresh(request)
    return request

# 🔹 Delete a request
@request_router.delete("/{request_id}")
def delete_request(request_id: int, db: Session = Depends(get_db)):
    request = db.query(Request).filter(Request.request_id == request_id).first()
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    db.delete(request)
    db.commit()
    return {"message": "Request deleted successfully"}

# 🔹 Get requests by city
@request_router.get("/city/{city_name}", response_model=list[RequestResponse])
def get_requests_by_city(city_name: str, db: Session = Depends(get_db)):
    requests = db.query(Request).filter(Request.city.ilike(f"%{city_name}%")).all()
    return requests

# 🔹 Get requests by blood group
@request_router.get("/blood_group/{blood_group}", response_model=list[RequestResponse])
def get_requests_by_blood_group(blood_group: str, db: Session = Depends(get_db)):
    requests = db.query(Request).filter(Request.blood_group == blood_group).all()
    return requests