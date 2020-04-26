from typing import cast
import importlib
import sys
import os
from pprint import pprint

sys.path.append(os.path.join(os.getcwd(), "scrapers"))
sys.path.append(os.getcwd())

from scrapers.scraper import Scraper


if __name__ == "__main__":
    scraper_module_name, scraper_class_name = sys.argv[1], sys.argv[2]
    scraper_module = importlib.import_module(f"scrapers.{scraper_module_name}")
    scraper_class = cast(Scraper, getattr(scraper_module, scraper_class_name))

    scraper = scraper_class()
    pprint(scraper.run())
