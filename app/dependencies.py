from fastapi import Depends, HTTPException
from jose import jwt
from sqlalchemy.orm import Session
from .database import get_db
from .models import User
from .auth import SECRET_KEY, ALGORITHM


def get_current_user(token: str, db: Session = Depends(get_db)):

    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    user_id = payload.get("user_id")

    user = db.query(User).filter(User.id == user_id).first()

    return user


def admin_required(user: User = Depends(get_current_user)):

    if user.role != "admin":

        raise HTTPException(status_code=403, detail="Admin access required")

    return user