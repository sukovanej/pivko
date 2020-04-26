from typing import Type

from scrapers.scraper import Scraper
from repositories import ProductsRepository


class ScraperTask:
    def __init__(self, scraper_class: Type[Scraper], products_repository: ProductsRepository) -> None:
        self.__scraper_class = scraper_class
        self.__products_repository = products_repository

    def run(self) -> None:
        scraper = self.__scraper_class()
        scraper_output = scraper.run()

        self.__products_repository.save_products(scraper_output)
