from utils import get_menu_links, extract_data, build_spreadsheet
from config import INTRO, SUCCESS, SPREADSHEET_NAME, TABLE_SETTINGS


def main():
    print(INTRO)
    menu_links = get_menu_links()
    data = extract_data(menu_links)
    build_spreadsheet(data, SPREADSHEET_NAME, TABLE_SETTINGS["headings"], TABLE_SETTINGS["column_width"])
    print(SUCCESS)


if __name__ == "__main__":
    main()
