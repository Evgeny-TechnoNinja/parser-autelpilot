from .get_document import get_document
from bs4 import BeautifulSoup, Tag
from config import TARGET_URL, MARKUP_ANALYZER  # noqa


def get_menu_links():
    """
    Selects and provides the necessary links from the menu
    :return: List of product links
    """
    all_links = []
    result = []
    document = get_document(TARGET_URL)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    nav = soup \
        .find("ul", {"class": "header-navigation-list clearfix"}) \
        .find_all("li", {"class": "header-navigation-list-item primary-list-item has-dropdown"})
    for elem in nav:
        parent = elem.find("ul", {"class": "header-navigation-list secondary-list clearfix"})
        for child in parent:
            if isinstance(child, Tag):
                valuable_link = child.find_all("a")
                for current_link in valuable_link:
                    all_links.append(current_link)

    def add_result(css_class_name, links):
        for received_link in links:
            if css_class_name in received_link["class"]:
                result.append(f"{TARGET_URL}{received_link['href']}")

    add_result("tertiary-link", all_links)
    all_links[:] = all_links[-3:]
    add_result("secondary-link", all_links)
    return result
