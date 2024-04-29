from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str
    desc: str

class Product(ProductBase):
    class config():
        from_attributes = True

class ShowProduct(BaseModel):
    title:str
    desc: str
    category: str
    class Config():
        from_attributes = True

