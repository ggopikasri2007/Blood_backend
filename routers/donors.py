# from fastapi import APIRouter , Depends
# from sqlalchemy.orm import Session
# from dependencies import get_db
# from models.donors import Donor
# from schemas.donors import DonorCreate
# donors_router=APIRouter(
#     prefix="/donors",
#     tags=["donors"]
# )
# @donors_router.get("/all")
# def all_donors(db:Session= Depends(get_db)):
#     val=db.query(Donor).all()
#     db.close()
#     return val
# @donors_router.get("/{donor_id}")
# def donor_id(donor_id:int , db:Session=Depends(get_db)):
#     val=db.query(Donor).filter(Donor.donor_id==donor_id).first()
#     db.close()
#     return val
# @donors_router.post("/create")
# def add_donors(donors:DonorCreate,db:Session=Depends(get_db)):
#     new_donor=Donor(
#     name=donors.name,
#     phone_number=donors.phone_number,
#     address=donors.address,
#     blood_group=donors.blood_group,
#     age=donors.age
#     )
#     db.add(new_donor)
#     db.commit()
#     db.refresh(new_donor)
#     return new_donor
# @donors_router.put("/updateDonor/{donor_id}")
# def update_donors(donor_id:int , donors:DonorCreate , db:Session=Depends(get_db)):
#     update_donors=db.query(Donor).filter(Donor.donor_id==donor_id).first()
#     update_donors.age=donors.age
#     update_donors.address=donors.address
#     db.commit()
#     db.refresh(update_donors)
#     return update_donors

# @donors_router.delete("/deleteDonor/{donor_id}")
# def delete_donors(donor_id: int, db: Session = Depends(get_db)):
#     donors = db.query(Donor).filter(Donor.donor_id == donor_id).first()

#     db.delete(donors)
#     db.commit()

#     return {"msg": "donor deleted successfully"}



from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.donors import Donor
from schemas.donors import DonorCreate

donors_router = APIRouter(
    prefix="/donors",
    tags=["Donors"]
)

# GET ALL DONORS
@donors_router.get("/all")
def all_donors(db: Session = Depends(get_db)):
    return db.query(Donor).all()


# GET DONOR BY ID
@donors_router.get("/{donor_id}")
def get_donor(donor_id: int, db: Session = Depends(get_db)):
    donor = db.query(Donor).filter(Donor.donor_id == donor_id).first()
    if not donor:
        raise HTTPException(status_code=404, detail="Donor not found")
    return donor


# CREATE DONOR (DONATION FORM)
@donors_router.post("/create")
def add_donor(donors: DonorCreate, db: Session = Depends(get_db)):
    new_donor = Donor(**donors.dict())
    db.add(new_donor)
    db.commit()
    db.refresh(new_donor)
    return new_donor


# UPDATE DONOR
@donors_router.put("/update/{donor_id}")
def update_donor(donor_id: int, donors: DonorCreate, db: Session = Depends(get_db)):
    donor = db.query(Donor).filter(Donor.donor_id == donor_id).first()
    if not donor:
        raise HTTPException(status_code=404, detail="Donor not found")

    donor.name = donors.name
    donor.phone_number = donors.phone_number
    donor.address = donors.address
    donor.blood_group = donors.blood_group
    donor.age = donors.age

    db.commit()
    db.refresh(donor)
    return donor


# DELETE DONOR
@donors_router.delete("/delete/{donor_id}")
def delete_donor(donor_id: int, db: Session = Depends(get_db)):
    donor = db.query(Donor).filter(Donor.donor_id == donor_id).first()
    if not donor:
        raise HTTPException(status_code=404, detail="Donor not found")

    db.delete(donor)
    db.commit()
    return {"message": "Donor deleted successfully"}


