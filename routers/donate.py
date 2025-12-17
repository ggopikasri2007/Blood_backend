from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.donors import Donor
from models.donate import Donate
from schemas.donate import DonateCreate, DonateUpdate
from datetime import datetime

donate_router = APIRouter(
    prefix="/donations",
    tags=["Donations"]
)

# GET ALL DONATIONS
@donate_router.get("/all")
def all_donations(db: Session = Depends(get_db)):
    return db.query(Donate).all()

# GET DONATION BY ID
@donate_router.get("/{donation_id}")
def get_donation(donation_id: int, db: Session = Depends(get_db)):
    return db.query(Donate).filter(Donate.donation_id == donation_id).first()

# CREATE DONATION (auto-add to donors)
@donate_router.post("/create")
def add_donation(donation: DonateCreate, db: Session = Depends(get_db)):
    # Create or get donor without using if
    donor = Donor(
        name=donation.full_name,
        phone_number=donation.contact_number,
        address=donation.city,
        blood_group=donation.blood_group,
        age=donation.age
    )
    donor = db.merge(donor)  # insert if not exists, otherwise return existing
    db.commit()
    db.refresh(donor)

    # Create donation linked to donor
    donation_db = Donate(
        donor_id=donor.donor_id,
        full_name=donation.full_name,
        age=donation.age,
        blood_group=donation.blood_group,
        city=donation.city,
        contact_number=donation.contact_number,
        donation_date=datetime.utcnow()
    )
    db.add(donation_db)
    db.commit()
    db.refresh(donation_db)
    return donation_db

# UPDATE DONATION
@donate_router.put("/update/{donation_id}")
def update_donation(donation_id: int, donation: DonateUpdate, db: Session = Depends(get_db)):
    donation_db = db.query(Donate).filter(Donate.donation_id == donation_id).first()

    # Update donor info automatically
    donor = Donor(
        donor_id=donation_db.donor_id,
        name=donation.full_name,
        phone_number=donation.contact_number,
        address=donation.city,
        blood_group=donation.blood_group,
        age=donation.age
    )
    db.merge(donor)
    db.commit()
    db.refresh(donor)

    # Update donation details
    donation_db.full_name = donation.full_name
    donation_db.age = donation.age
    donation_db.blood_group = donation.blood_group
    donation_db.city = donation.city
    donation_db.contact_number = donation.contact_number
    db.commit()
    db.refresh(donation_db)
    return donation_db

# DELETE DONATION
@donate_router.delete("/delete/{donation_id}")
def delete_donation(donation_id: int, db: Session = Depends(get_db)):
    donation_db = db.query(Donate).filter(Donate.donation_id == donation_id).first()
    db.delete(donation_db)
    db.commit()
    return {"message": "Donation deleted successfully"}
