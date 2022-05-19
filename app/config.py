TARGET_URL = "https://www.autelpilot.com"
USER_AGENT = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Trident/4.0)"
MARKUP_ANALYZER = "lxml"
PROGRESS_BAR_SETTING = "{l_bar}{bar:10}{r_bar}{bar:-10b}"
RESULT_FOLDER = "output"
SPREADSHEET_NAME = "autelpilot"
HEADING_STYLE = {"bold": True}
TABLE_SETTINGS = {
        "headings": [("A1", "Имя товара"), ("B1", "Ссылка #1"), ("C1", "Ссылка #2")],
        "column_width": [("A:A", 40), ("B:B", 50), ("C:C", 50)],
}
INTRO = f"""
───────────────────────╔╗───╔╗────╔╗───╔╗
──────────────────────╔╝╚╗──║║────║║──╔╝╚╗
╔══╦══╦═╦══╦══╦═╗╔══╦╗╠╗╔╬══╣║╔══╦╣║╔═╩╗╔╝
║╔╗║╔╗║╔╣══╣║═╣╔╝║╔╗║║║║║║║═╣║║╔╗╠╣║║╔╗║║
║╚╝║╔╗║║╠══║║═╣║─║╔╗║╚╝║╚╣║═╣╚╣╚╝║║╚╣╚╝║╚╗
║╔═╩╝╚╩╝╚══╩══╩╝─╚╝╚╩══╩═╩══╩═╣╔═╩╩═╩══╩═╝
║║────────────────────────────║║
╚╝────────────────────────────╚╝
        Getting the necessary links
        {TARGET_URL}
"""
SUCCESS = f"Ready! See the {RESULT_FOLDER} folder..."
