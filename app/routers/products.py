from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Product
from ..schemas import ProductCreate
from ..dependencies import admin_required
from ..utils.logger import log_action

router = APIRouter()


@router.post("/products")
def create_product(product: ProductCreate,
                   db: Session = Depends(get_db),
                   admin=Depends(admin_required)):

    new_product = Product(**product.dict())

    db.add(new_product)
    db.commit()

    log_action(f"Admin {admin.username} created product {product.name}")

    return {"message": "Product created"}


@router.get("/products")
def get_products(db: Session = Depends(get_db)):

    products = db.query(Product).all()

    return products