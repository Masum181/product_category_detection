from fastapi import APIRouter, Depends, status, HTTPException

import schemas, database, models
from sqlalchemy.orm import Session
from typing import List
from nlp_model import pred_category



router = APIRouter(
    prefix='/product',
    tags= ['products']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowProduct])
def all(db:Session=Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@router.get("/{id}", status_code=200, response_model=schemas.ShowProduct)
def show(id, db:Session=Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'product with the id {id} is not available')
    return product

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Product, db:Session=Depends(get_db)):
    category = pred_category(request.desc)
    new_product = models.Product(title=request.title, desc = request.desc, category=category)

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
