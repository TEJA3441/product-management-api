from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from .database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    role = Column(String, default="user")


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    description = Column(String)

    price = Column(Float)

    category = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Log(Base):

    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)

    action = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    product_id = Column(Integer)

    timestamp = Column(DateTime(timezone=True), server_default=func.now())