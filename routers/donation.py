# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from datetime import datetime, timedelta
# from models.donation import Donation
# from models.user import User
# from schemas.donation import DonationResponse
# from dependencies import get_db

# donation_router = APIRouter(
#     prefix="/donation",
#     tags=["Donation"]
# )

# #  Confirm donation
# @donation_router.post("/confirm/{user_id}", response_model=DonationResponse)
# def confirm_donation(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.user_id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     new_donation = Donation(user_id=user_id)
#     db.add(new_donation)
#     db.commit()
#     db.refresh(new_donation)

#     return new_donation

# #  Check eligibility
# @donation_router.get("/eligibility/{user_id}")
# def check_eligibility(user_id: int, db: Session = Depends(get_db)):
#     last_donation = (
#         db.query(Donation)
#         .filter(Donation.user_id == user_id)
#         .order_by(Donation.donation_date.desc())
#         .first()
#     )

#     if not last_donation:
#         return {"eligible": True, "message": "You are eligible to donate."}

#     next_eligible_date = last_donation.donation_date + timedelta(days=90)
#     if datetime.utcnow() >= next_eligible_date:
#         return {"eligible": True, "message": "You are eligible to donate."}

#     remaining_days = (next_eligible_date - datetime.utcnow()).days
#     return {
#         "eligible": False,
#         "remaining_days": remaining_days,
#         "next_eligible_date": next_eligible_date,
#         "message": f"You can donate after {remaining_days} days."
#     }

# #  Donation history
# @donation_router.get("/history/{user_id}", response_model=list[DonationResponse])
# def donation_history(user_id: int, db: Session = Depends(get_db)):
#     donations = (
#         db.query(Donation)
#         .filter(Donation.user_id == user_id)
#         .order_by(Donation.donation_date.desc())
#         .all()
#     )
#     return donations

# # Get all donors with availability
# @donation_router.get("/available-donors")
# def get_available_donors(db: Session = Depends(get_db)):
#     users = db.query(User).all()
#     donors = []

#     for user in users:
#         last_donation = (
#             db.query(Donation)
#             .filter(Donation.user_id == user.user_id)
#             .order_by(Donation.donation_date.desc())
#             .first()
#         )

#         # Default status
#         status = "Available"

#         # If user has donated, calculate next eligible date
#         if last_donation:
#             next_date = last_donation.donation_date + timedelta(days=90)
#             if datetime.utcnow() < next_date:
#                 remaining_days = (next_date - datetime.utcnow()).days
#                 status = f"Available after {remaining_days} days"

#         donors.append({
#             "full_name": user.full_name,
#             "age": user.age,
#             "blood_group": user.blood_group,
#             "city": user.city,
#             "phone": user.phone,
#             "status": status
#         })

#     return donors

    from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from models.donation import Donation
from models.user import User
from schemas.donation import DonationResponse
from dependencies import get_db

donation_router = APIRouter(
    prefix="/donation",
    tags=["Donation"]
)

# ==============================
# Confirm donation
# ==============================
@donation_router.post("/confirm/{user_id}", response_model=DonationResponse)
def confirm_donation(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_donation = Donation(
        user_id=user_id,
        donation_date=datetime.utcnow()  # store in UTC
    )
    db.add(new_donation)
    db.commit()
    db.refresh(new_donation)

    return new_donation

# ==============================
# Check eligibility
# ==============================
@donation_router.get("/eligibility/{user_id}")
def check_eligibility(user_id: int, db: Session = Depends(get_db)):
    last_donation = (
        db.query(Donation)
        .filter(Donation.user_id == user_id)
        .order_by(Donation.donation_date.desc())
        .first()
    )

    if not last_donation:
        return {
            "eligible": True,
            "message": "You are eligible to donate."
        }

    next_eligible_date = last_donation.donation_date + timedelta(days=90)

    if datetime.utcnow() >= next_eligible_date:
        return {
            "eligible": True,
            "message": "You are eligible to donate."
        }

    remaining_days = (next_eligible_date - datetime.utcnow()).days

    return {
        "eligible": False,
        "remaining_days": remaining_days,
        "next_eligible_date": next_eligible_date.strftime("%Y-%m-%d"),
        "message": f"You can donate after {remaining_days} days."
    }

# ==============================
# Donation history
# ==============================
@donation_router.get("/history/{user_id}", response_model=list[DonationResponse])
def donation_history(user_id: int, db: Session = Depends(get_db)):
    donations = (
        db.query(Donation)
        .filter(Donation.user_id == user_id)
        .order_by(Donation.donation_date.desc())
        .all()
    )
    return donations

# ==============================
# Get all donors with availability
# ==============================
@donation_router.get("/available-donors")
def get_available_donors(db: Session = Depends(get_db)):
    users = db.query(User).all()
    donors = []

    for user in users:
        last_donation = (
            db.query(Donation)
            .filter(Donation.user_id == user.user_id)
            .order_by(Donation.donation_date.desc())
            .first()
        )

        status = "Available"
        next_eligible_date = None

        if last_donation:
            next_date = last_donation.donation_date + timedelta(days=90)
            if datetime.utcnow() < next_date:
                status = "Not Available"
                next_eligible_date = next_date.strftime("%Y-%m-%d")

        donors.append({
            "full_name": user.full_name,
            "age": user.age,
            "blood_group": user.blood_group,
            "city": user.city,
            "phone": user.phone,
            "status": status,
            "next_eligible_date": next_eligible_date
        })

    return donors