# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from dependencies import get_db
# from models.user import User
# from schemas.user import UserCreate, UserLogin, UserResponse

# auth_router = APIRouter(
#     prefix="/auth",
#     tags=["Authentication"]
# )

# # 🔹 SIGNUP
# @auth_router.post("/signup", response_model=UserResponse)
# def signup(user: UserCreate, db: Session = Depends(get_db)):

#     existing_user = db.query(User).filter(User.email == user.email).first()

#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")

#     new_user = User(
#         full_name=user.full_name,
#         email=user.email,
#         password=user.password,
#         age=user.age,
#         blood_group=user.blood_group,
#         city=user.city,
#         phone=user.phone
#     )

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user



# @auth_router.post("/login")
# def login(user: UserLogin, db: Session = Depends(get_db)):

#     db_user = db.query(User).filter(User.email == user.email).first()

#     if not db_user or db_user.password != user.password:
#         raise HTTPException(status_code=400, detail="Invalid email or password")

#     return {
#         "message": "Login successful",
#         "user_id": db_user.user_id   
#     }

# from fastapi import Path


# @auth_router.get("/user/{user_id}", response_model=UserResponse)
# def get_user(user_id: int = Path(...), db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.user_id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @auth_router.put("/user/{user_id}", response_model=UserResponse)
# def update_user(user_id: int, updated_user: UserCreate, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.user_id == user_id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")

#     user.full_name = updated_user.full_name
#     user.email = updated_user.email
#     user.age = updated_user.age
#     user.blood_group = updated_user.blood_group
#     user.city = updated_user.city
#     user.phone = updated_user.phone

#     db.commit()
#     db.refresh(user)
#     return user

from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from dependencies import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin, UserResponse, UserUpdate

auth_router = APIRouter(
        prefix="/auth",
        tags=["Authentication"]
    )

    # 🔹 SIGNUP
@auth_router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        new_user = User(
            full_name=user.full_name,
            email=user.email,
            password=user.password,
            age=user.age,
            blood_group=user.blood_group,
            city=user.city,
            phone=user.phone
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    # 🔹 LOGIN
@auth_router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
        db_user = db.query(User).filter(User.email == user.email).first()
        if not db_user or db_user.password != user.password:
            raise HTTPException(status_code=400, detail="Invalid email or password")
        return {
            "message": "Login successful",
            "user_id": db_user.user_id
        }

    # 🔹 GET USER
@auth_router.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int = Path(...), db: Session = Depends(get_db)):
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    # 🔹 UPDATE USER (edit profile)
@auth_router.put("/user/{user_id}", response_model=UserResponse)
def update_user(user_id: int, updated_user: UserUpdate, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.user_id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Only update allowed fields (blood_group cannot be changed)
        user.full_name = updated_user.full_name
        user.email = updated_user.email
        user.age = updated_user.age
        user.city = updated_user.city
        user.phone = updated_user.phone

        db.commit()
        db.refresh(user)
        return user