from enum import Enum
from operator import attrgetter
from abc import ABC, abstractmethod
from typing import List

from pydantic import BaseModel

from .shops import Shop


class ScraperOutputProduct(BaseModel):
    title: str
    description: str
    price: float
    volume: float
    shop: Shop

    class Config:
        json_encoders = {Shop: attrgetter("value")}


class ScraperOutput(BaseModel):
    products: List[ScraperOutputProduct]

    class Config:
        orm_mode = True


class Scraper(ABC):
    @abstractmethod
    def run(self) -> ScraperOutput:
        pass
