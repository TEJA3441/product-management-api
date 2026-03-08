from pydantic import BaseModel


class UserRegister(BaseModel):

    username: str
    email: str
    password: str


class UserLogin(BaseModel):

    email: str
    password: str


class ProductCreate(BaseModel):

    name: str
    description: str
    price: float
    category: str


class ProductUpdate(BaseModel):

    name: str
    description: str
    price: float
    category: str