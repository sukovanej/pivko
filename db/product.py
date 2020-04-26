from sqlalchemy import Column, Integer, String, Sequence, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

from .base import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(String, nullable=False)
    volume = Column(String, nullable=False)
    shop = Column(String, nullable=False)
    created = Column(DateTime, server_default=func.now(), index=True, nullable=False)
