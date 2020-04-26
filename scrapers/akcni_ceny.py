import re
from typing import List
import requests
from bs4 import BeautifulSoup

from .scraper import Scraper, ScraperOutput, ScraperOutputProduct, ScraperOutputProduct
from .shops import Shop


class AkcniCeny(Scraper):
    AKCNI_CENY_BASE_URL = "https://www.akcniceny.cz"
    KAUFLAND_URL = f"{AKCNI_CENY_BASE_URL}/zbozi/napoje-alkoholicke/piva/"

    def run(self) -> ScraperOutput:
        page_response = requests.get(self.KAUFLAND_URL)
        page = BeautifulSoup(page_response.content, 'html.parser')
        output = ScraperOutput(products=[])
        output.products.extend(self.run_page(page))

        pages = page.find_all(attrs={"class": "page-item"})
        for sub_page_item in [p for p in pages if p.a]:
            sub_page_response = requests.get(f"{self.AKCNI_CENY_BASE_URL}/{sub_page_item.a.get('href')}")
            sub_page = BeautifulSoup(sub_page_response.content, 'html.parser')

            output.products.extend(self.run_page(sub_page))


    def run_page(self, page) -> List[ScraperOutputProduct]:
        products = page.find_all(attrs={"itemtype": "http://schema.org/Product"})
        output = []

        for product in products:
            title = product.find(attrs={"class": "nadpis-zbozi"}).a.get("title")
            description = product.find(attrs={"class": "popis"}).string.strip()
            price_str: str = product.find(attrs={"class": "cena-zbozi"}).contents[1].strip()
            shop = product.find(attrs={"class": "prodejna-name"}).string.strip()

            re_volume_with_l = re.compile(r"\d+,\d+l")
            re_volume_with_plechovka = re.compile(r"plechovka")
            re_volumn_with_kusu = re.compile(r"(\d kusů)")
            re_volume_with_ml = re.compile(r"\d+ml")

            if m := re.search(re_volume_with_l, title):
                volume = float(m.group()[:-1].replace(",", "."))
            elif re.search(re_volume_with_plechovka, title):
                volume = 0.5
            elif (m := re.search(re_volume_with_ml, title)):
                volume = float(m.group()[:-2]) / 1000
            elif re.search(re_volume_with_plechovka, title) and (m := re.search(re_volumn_with_kusu, title)):
                breakpoint()
            else:
                raise Exception(f"Can't parse volume from the title: {title}")

            price = float(price_str.replace(",", "."))

            product = ScraperOutputProduct(title=title, description=description, price=price, volume=volume, shop=Shop(shop))
            output.append(product)

            print(product)

        return output
