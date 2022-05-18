from .get_document import get_document
from bs4 import BeautifulSoup
from config import MARKUP_ANALYZER, TARGET_URL  # noqa


def analysis_product_card(link):
    """
    Retrieves the necessary links and product name from the product card
    :param link: link to product card
    :return: Object with desired data or False
    """
    blank = {
        "name": "",
        "links": []
    }
    document = get_document(link)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    form = soup.find("div", {"class": "product-wrap"}).find("form")
    product_versions = form.find_all("div", {"product-version"})
    if product_versions:
        for current_product in product_versions:
            links = current_product.find_all("a", {"class": "active"})[0]["href"]
            blank["links"].append(f"{TARGET_URL}{links}")
        name = soup.find("h1", {"class": "product-title"}).text
        blank["name"] = name.strip()
        return blank
    return False
