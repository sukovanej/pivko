import re
import requests
from bs4 import BeautifulSoup

from .scraper import Scraper, ScraperOutput, ScraperOutputProduct
from .shops import Shop


class KauflandScraper(Scraper):
    KAUFLAND_URL = "https://www.kaufland.cz/nabidka/aktualni-tyden.category=08_N%C3%A1poje__lihoviny.html"

    def run(self) -> ScraperOutput:
        page_response = requests.get(self.KAUFLAND_URL)
        soup = BeautifulSoup(page_response.content, 'html.parser')
        products = soup.find_all(attrs={"class": "o-overview-list__list-item"})

        output = ScraperOutput(products=[])

        for product in products:
            title = product.find(attrs={"class": "m-offer-tile__subtitle"}).string.strip()
            description = product.find(attrs={"class": "m-offer-tile__title"}).string.strip()
            price_str: str = product.find(attrs={"class": "a-pricetag__price"}).string.strip()
            volume_str: str = product.find(attrs={"class": "m-offer-tile__quantity"}).string.strip().split()[0]

            re_volume_only = re.compile(r"\d+(\,)*\d+")
            re_volume_only_int = re.compile(r"\d+")
            re_volume_with_l = re.compile(r"\d+(\,)*?\d+l")
            re_volume_multiples = re.compile(r"\d+x\d+(\,)\d+")

            if re.fullmatch(re_volume_only, volume_str) or re.fullmatch(re_volume_only_int, volume_str):
                volume = float(volume_str.replace(",", "."))
            elif re.fullmatch(re_volume_with_l, volume_str):
                volume = float(volume_str[:-1].replace(",", "."))
            elif re.fullmatch(re_volume_multiples, volume_str):
                n, vol = volume_str.split("x")
                volume = int(n) * float(vol.replace(",", "."))
            else:
                raise Exception(f"Unkown volume format {volume_str}")

            price = float(price_str.replace(",", "."))
            output.products.append(ScraperOutputProduct(title=title, description=description, price=price, volume=volume, shop=Shop.KAUFLAND))

        return output
