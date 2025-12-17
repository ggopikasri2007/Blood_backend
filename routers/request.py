from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.request import Request
from schemas.request import RequestCreate, RequestUpdate

request_router = APIRouter(
    prefix="/requests",
    tags=["Request Blood"]
)

# GET ALL REQUESTS
@request_router.get("/all")
def all_requests(db: Session = Depends(get_db)):
    return db.query(Request).all()

# GET REQUEST BY ID
@request_router.get("/{request_id}")
def get_request(request_id: int, db: Session = Depends(get_db)):
    return db.query(Request).filter(Request.request_id == request_id).first()

# CREATE REQUEST
@request_router.post("/create")
def create_request(request: RequestCreate, db: Session = Depends(get_db)):
    request_db = Request(
        donor_name=request.donor_name,
        blood_group=request.blood_group,
        city=request.city,
        contact_number=request.contact_number,
        message=request.message
    )
    db.add(request_db)
    db.commit()
    db.refresh(request_db)
    return request_db

# UPDATE REQUEST
@request_router.put("/update/{request_id}")
def update_request(request_id: int, request: RequestUpdate, db: Session = Depends(get_db)):
    request_db = db.query(Request).filter(Request.request_id == request_id).first()
    request_db.donor_name = request.donor_name
    request_db.blood_group = request.blood_group
    request_db.city = request.city
    request_db.contact_number = request.contact_number
    request_db.message = request.message
    db.commit()
    db.refresh(request_db)
    return request_db

# DELETE REQUEST
@request_router.delete("/delete/{request_id}")
def delete_request(request_id: int, db: Session = Depends(get_db)):
    request_db = db.query(Request).filter(Request.request_id == request_id).first()
    db.delete(request_db)
    db.commit()
    return {"message": "Request deleted successfully"}
