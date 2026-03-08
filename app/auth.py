from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"])


def hash_password(password):

    return pwd_context.hash(password)


def verify_password(password, hashed):

    return pwd_context.verify(password, hashed)


def create_token(data: dict):

    payload = data.copy()

    expire = datetime.utcnow() + timedelta(hours=2)

    payload.update({"exp": expire})

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token