from typing import List
from datetime import date
from uuid import uuid4

from sqlalchemy import cast, Date

from db import Product
from scrapers import ScraperOutput
from .repository import Repository


class ProductsRepository(Repository):
    def get_today_data(self) -> List[Product]:
        raise NotImplementedError

    def save_products(self, scraper_output: ScraperOutput) -> None:
        products = self._session.collection("products")
        for product in scraper_output.products:
            doc_ref = products.document(str(uuid4()))
            print(product.dict())
            doc_ref.set(product.dict())
