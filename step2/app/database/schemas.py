from pydantic import BaseModel, Field, EmailStr
from datetime import datetime           


class UserBase(BaseModel):
    firstname: str = Field(..., description="First name user", min_length=1, max_length=30)
    secondname: str = Field(..., description="Second name user", min_length=1, max_length=30)
    email: EmailStr = Field(..., description="email")

class ProductBase(BaseModel):
    id: int

class ProductIn(ProductBase):
    product_name: str = Field(..., description="Description of product", min_length=1, max_length=300)  
    description: str = Field(..., description="Description of product", min_length=1, max_length=300)
    price: float = Field(..., description="Product price ", ge=0)

class OrderBase(BaseModel):
    create_at: datetime 
    update_at: datetime
    status: bool = Field(..., description="status of order")

class OrderCreate(OrderBase):
    user_id: int 
    product_id: int
    
    class Config:
        from_attributes = True

class Order(OrderBase):
    id_order: int

class UserCreate(UserBase):
    pwd: str =Field(..., description="Hash of pwd", min_length=1, max_length=500)

class User(UserBase):
    id_user: int

    class Config:
        from_attributes = True

class UserIn(UserBase):
    pass


