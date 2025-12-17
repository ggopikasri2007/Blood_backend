# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from dependencies import get_db
# from models.blood_bank import BloodBank
# from schemas.blood_bank import BloodBankCreate, BloodBankUpdate

# blood_bank_router = APIRouter(
#     prefix="/blood_bank",
#     tags=["BloodBank"]
# )

# @blood_bank_router.get("/")
# def all_blood_bank(db: Session = Depends(get_db)):
#     val = db.query(BloodBank).all()
#     db.close()
#     return val

# @blood_bank_router.post("/create")
# def add_blood_bank(blood_bank: BloodBankCreate, db: Session = Depends(get_db)):
#     new_blood_bank = BloodBank(
#         name=blood_bank.name,
#         address=blood_bank.address,
#         contact_number=blood_bank.contact_number,
#         image=blood_bank.image,
#         city=blood_bank.city,
#         email=blood_bank.email
#     )
#     db.add(new_blood_bank)
#     db.commit()
#     db.refresh(new_blood_bank)
#     return new_blood_bank
# @blood_bank_router.get("/{blood_bank_id}")
# def blood_bank_id(blood_bank_id:int, db:Session=Depends(get_db)):
#     val=db.query(BloodBank).filter(BloodBank.blood_bank_id==blood_bank_id).first()
#     db.close()
#     return val
# @blood_bank_router.put("/updateBloodBank/{blood_bank_id}")
# def update_blood_bank(blood_bank_id:int , blood_bank:BloodBankUpdate , db:Session=Depends(get_db)):
#     update_blood_bank=db.query(BloodBank).filter(BloodBank.blood_bank_id==blood_bank_id).first()
#     update_blood_bank.name=blood_bank.name
#     update_blood_bank.address=blood_bank.address
#     update_blood_bank.city=blood_bank.city
#     update_blood_bank.contact_number=blood_bank.contact_number
#     update_blood_bank.email=blood_bank.email
#     db.commit()
#     db.refresh(update_blood_bank)
#     return update_blood_bank
# @blood_bank_router.delete("/deleteBloodBank/{blood_bank_id}")
# def delete_blood_bank(blood_bank_id: int, db: Session = Depends(get_db)):
#     blood_bank = db.query(BloodBank).filter(BloodBank.blood_bank_id == blood_bank_id).first()

#     db.delete(blood_bank)
#     db.commit()
#     return{"msg":"blood_bank deleted successfully"}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from models.blood_bank import BloodBank
from schemas.blood_bank import BloodBankCreate, BloodBankUpdate

blood_bank_router = APIRouter(
    prefix="/blood_bank",
    tags=["BloodBank"]
)

@blood_bank_router.get("/")
def all_blood_bank(db: Session = Depends(get_db)):
    return db.query(BloodBank).all()

@blood_bank_router.post("/create")
def add_blood_bank(blood_bank: BloodBankCreate, db: Session = Depends(get_db)):
    new_blood_bank = BloodBank(
        name=blood_bank.name,
        address=blood_bank.address,
        contact_number=blood_bank.contact_number,
        image=blood_bank.image,
        city=blood_bank.city,
        email=blood_bank.email
    )
    db.add(new_blood_bank)
    db.commit()
    db.refresh(new_blood_bank)
    return new_blood_bank

@blood_bank_router.get("/{blood_bank_id}")
def get_blood_bank(blood_bank_id: int, db: Session = Depends(get_db)):
    return db.query(BloodBank).filter(BloodBank.blood_bank_id == blood_bank_id).first()

@blood_bank_router.put("/update/{blood_bank_id}")
def update_blood_bank(blood_bank_id: int, blood_bank: BloodBankUpdate, db: Session = Depends(get_db)):
    db_blood_bank = db.query(BloodBank).filter(BloodBank.blood_bank_id == blood_bank_id).first()
    db_blood_bank.name = blood_bank.name
    db_blood_bank.address = blood_bank.address
    db_blood_bank.city = blood_bank.city
    db_blood_bank.contact_number = blood_bank.contact_number
    db_blood_bank.email = blood_bank.email
    db.commit()
    db.refresh(db_blood_bank)
    return db_blood_bank

@blood_bank_router.delete("/delete/{blood_bank_id}")
def delete_blood_bank(blood_bank_id: int, db: Session = Depends(get_db)):
    db_blood_bank = db.query(BloodBank).filter(BloodBank.blood_bank_id == blood_bank_id).first()
    db.delete(db_blood_bank)
    db.commit()
    return {"msg": "Blood bank deleted successfully"}


