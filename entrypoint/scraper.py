import os

# from db import db_session_factory
from firestore import firestore_client_factory
from repositories import ProductsRepository
from task import ScraperTask
from scrapers import KauflandScraper


if __name__ == "__main__":
    POSTGRES_URL = os.environ["POSTGRES_URL"]

    # session = db_session_factory(POSTGRES_URL)
    session = firestore_client_factory()
    products_repository = ProductsRepository(session)
    scraper = ScraperTask(scraper_class=KauflandScraper, products_repository=products_repository)

    scraper.run()
