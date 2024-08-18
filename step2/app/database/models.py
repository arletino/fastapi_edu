
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from database.database import Base



class User(Base):
    __tablename__ = 'users'

    id_user: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(30))
    secondname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    pwd: Mapped[str] = mapped_column(String(500))
    orders = relationship('Order', backref='user', cascade='all, delete')

class Order(Base):
    __tablename__ = 'orders'

    id_order: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id_user'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id_product'))
    create_at = mapped_column(
        DateTime(), default=func.now(), 
        server_default=FetchedValue()
    )
    update_at = mapped_column(
        DateTime(),
        onupdate=func.now(),
        server_default=FetchedValue(),
        server_onupdate=FetchedValue(),
    )
    status: Mapped[bool] = mapped_column(default=True)

class Product(Base):
    __tablename__ = 'products'

    id_product: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(300))
    price: Mapped[float] = mapped_column(Float())
    orders = relationship('Order', backref='product', cascade='all, delete')



