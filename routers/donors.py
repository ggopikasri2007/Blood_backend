# # from fastapi import APIRouter, Depends
# # from sqlalchemy.orm import Session
# # from dependencies import get_db
# # from models.donors import Donor
# # from models.donate import Donate
# # from schemas.donors import DonorCreate

# # donors_router = APIRouter(
# #     prefix="/donors",
# #     tags=["donors"]
# # )

# # @donors_router.get("/all")
# # def all_donors(db: Session = Depends(get_db)):
# #     return db.query(Donor).all()


# # @donors_router.get("/{donor_id}") 
# # def donor_id(donor_id: int, db: Session = Depends(get_db)):
# #     return db.query(Donor).filter(Donor.donor_id == donor_id).first()


# # @donors_router.post("/create")
# # def add_donors(donors: DonorCreate, db: Session = Depends(get_db)):
# #     new_donor = Donor(
# #         name=donors.name,
# #         phone_number=donors.phone_number,
# #         address=donors.address,
# #         blood_group=donors.blood_group,
# #         age=donors.age
# #     )
# #     db.add(new_donor)
# #     db.commit()
# #     db.refresh(new_donor)
# #     return new_donor


# # @donors_router.put("/update/{donor_id}")
# # def update_donors(donor_id: int, donors: DonorCreate, db: Session = Depends(get_db)):
# #     db.query(Donor).filter(Donor.donor_id == donor_id).update(
# #         {
# #             Donor.name: donors.name,
# #             Donor.phone_number: donors.phone_number,
# #             Donor.address: donors.address,
# #             Donor.blood_group: donors.blood_group,
# #             Donor.age: donors.age
# #         },
# #         synchronize_session=False
# #     )
# #     db.commit()
# #     return {"msg": "Donor updated successfully"}


# # @donors_router.delete("/delete/{donor_id}")
# # def delete_donors(donor_id: int, db: Session = Depends(get_db)):
# #      db.query(Donate).filter(Donate.donor_id == donor_id).delete()
# #      db.query(Donor).filter(Donor.donor_id == donor_id).delete()
# #      db.commit()
# #     return {"msg": "Donor deleted successfully"}
# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from dependencies import get_db
# from models.donors import Donor
# from models.donate import Donate
# from schemas.donors import DonorCreate

# donors_router = APIRouter(
#     prefix="/donors",
#     tags=["donors"]
# )


# # Get all donors
# @donors_router.get("/all")
# def all_donors(db: Session = Depends(get_db)):
#     return db.query(Donor).all()


# # Get donor by ID
# @donors_router.get("/{donor_id}")
# def get_donor(donor_id: int, db: Session = Depends(get_db)):
#     donor = db.query(Donor).filter(Donor.donor_id == donor_id).first()

#     if not donor:
#         raise HTTPException(status_code=404, detail="Donor not found")

#     return donor


# # Create new donor
# @donors_router.post("/create")
# def add_donor(donor: DonorCreate, db: Session = Depends(get_db)):
#     new_donor = Donor(
#         name=donor.name,
#         phone_number=donor.phone_number,
#         address=donor.address,
#         blood_group=donor.blood_group,
#         age=donor.age
#     )

#     db.add(new_donor)
#     db.commit()
#     db.refresh(new_donor)

#     return new_donor


# # Update donor
# @donors_router.put("/update/{donor_id}")
# def update_donor(donor_id: int, donor: DonorCreate, db: Session = Depends(get_db)):
#     existing_donor = db.query(Donor).filter(Donor.donor_id == donor_id).first()

#     if not existing_donor:
#         raise HTTPException(status_code=404, detail="Donor not found")

#     existing_donor.name = donor.name
#     existing_donor.phone_number = donor.phone_number
#     existing_donor.address = donor.address
#     existing_donor.blood_group = donor.blood_group
#     existing_donor.age = donor.age

#     db.commit()
#     db.refresh(existing_donor)

#     return {"msg": "Donor updated successfully"}


# # Delete donor
# @donors_router.delete("/delete/{donor_id}")
# def delete_donor(donor_id: int, db: Session = Depends(get_db)):
#     donor = db.query(Donor).filter(Donor.donor_id == donor_id).first()

#     if not donor:
#         raise HTTPException(status_code=404, detail="Donor not found")

#     # First delete related donations
#     db.query(Donate).filter(Donate.donor_id == donor_id).delete()

#     # Then delete donor
#     db.delete(donor)
#     db.commit()

#     return {"msg": "Donor deleted successfully"}