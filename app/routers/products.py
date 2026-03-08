from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Product
from ..schemas import ProductCreate, ProductUpdate
from ..dependencies import admin_required
from ..utils.logger import log_action

router = APIRouter(prefix="/products", tags=["Products"])


# CREATE PRODUCT (ADMIN ONLY)
@router.post("/")
def create_product(
        product: ProductCreate,
        db: Session = Depends(get_db),
        admin=Depends(admin_required)
):

    new_product = Product(**product.dict())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    log_action(f"Admin {admin.username} created product {product.name}")

    return new_product


# GET ALL PRODUCTS WITH PAGINATION + FILTER + SORT
@router.get("/")
def get_products(
        db: Session = Depends(get_db),
        page: int = 1,
        limit: int = 10,
        category: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        sort: str | None = Query(None)
):

    query = db.query(Product)

    # Filtering
    if category:
        query = query.filter(Product.category == category)

    if min_price:
        query = query.filter(Product.price >= min_price)

    if max_price:
        query = query.filter(Product.price <= max_price)

    # Sorting
    if sort == "price_asc":
        query = query.order_by(Product.price.asc())

    if sort == "price_desc":
        query = query.order_by(Product.price.desc())

    # Pagination
    products = query.offset((page - 1) * limit).limit(limit).all()

    return products


# GET PRODUCT BY ID
@router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# UPDATE PRODUCT (ADMIN ONLY)
@router.put("/{product_id}")
def update_product(
        product_id: int,
        updated_product: ProductUpdate,
        db: Session = Depends(get_db),
        admin=Depends(admin_required)
):

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = updated_product.name
    product.description = updated_product.description
    product.price = updated_product.price
    product.category = updated_product.category

    db.commit()

    log_action(f"Admin {admin.username} updated product {product.name}")

    return {"message": "Product updated successfully"}


# DELETE PRODUCT (ADMIN ONLY)
@router.delete("/{product_id}")
def delete_product(
        product_id: int,
        db: Session = Depends(get_db),
        admin=Depends(admin_required)
):

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    log_action(f"Admin {admin.username} deleted product {product.name}")

    return {"message": "Product deleted successfully"}