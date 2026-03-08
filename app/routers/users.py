from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import UserRegister, UserLogin
from ..auth import hash_password, verify_password, create_token

router = APIRouter()


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        role="user"
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.password):

        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user_id": db_user.id})

    return {"token": token}