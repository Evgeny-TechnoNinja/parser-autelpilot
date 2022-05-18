from .get_document import get_document
from .analysis_product_card import analysis_product_card
from bs4 import BeautifulSoup
from config import MARKUP_ANALYZER, PROGRESS_BAR_SETTING, TARGET_URL  # noqa
from tqdm import tqdm


def extract_data(links):
    """
    Follows the link gets useful information to successfully get the right links
    :param links: Menu links
    :return: List of dictionaries with selected useful data
    """
    result = []
    goods_links = []
    for link in tqdm(links, desc="Extract useful information", bar_format=PROGRESS_BAR_SETTING):
        document = get_document(link)
        soup = BeautifulSoup(document, MARKUP_ANALYZER)
        try:
            section = soup.find("div", id="shopify-section-static-collection")
            if section["id"] == "shopify-section-static-collection":
                collection = soup.find("div", {"class": "list collection-list list-text-wrapper-below column-4"})
                product_links = collection.find_all("a", {"class": "list-container"})
                for current_link in product_links:
                    goods_links.append(f"{TARGET_URL}{current_link['href']}")
        except TypeError as e:
            section = soup.find("div", id="shopify-section-static-product")
            if section["id"] == "shopify-section-static-product":
                data = analysis_product_card(link)
                if data:
                    result.append(data)
    for link in tqdm(goods_links, desc="Extract useful information", bar_format=PROGRESS_BAR_SETTING):
        data = analysis_product_card(link)
        if data:
            result.append(data)
    return result
