import xlsxwriter
from .create_output_folder import create_output_folder
from config import HEADING_STYLE, PROGRESS_BAR_SETTING  # noqa
from tqdm import tqdm


@create_output_folder
def build_spreadsheet(data, name, header, column_width):
    """
    Build an Excel spreadsheet
    :param data: goods received
    :param name: filename table
    :param header: header settings
    :param column_width: column width settings
    """
    workbook = xlsxwriter.Workbook(name + ".xlsx")
    worksheet = workbook.add_worksheet()
    style = workbook.add_format(HEADING_STYLE)
    row = 1
    col = 0
    # header
    for item in header:
        worksheet.write(item[0], item[1], style)
    for item in column_width:
        worksheet.set_column(item[0], item[1])
    # body
    for value in tqdm(data, desc="Writing to a spreadsheet", bar_format=PROGRESS_BAR_SETTING):
        worksheet.write(row, col, value.get("name"))
        worksheet.write(row, col + 1, value.get("links")[0])
        worksheet.write(row, col + 2, value.get("links")[1])
        row += 1
    workbook.close()
