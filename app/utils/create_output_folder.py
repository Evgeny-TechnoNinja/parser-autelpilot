import os
import os.path
import shutil
from config import RESULT_FOLDER, SPREADSHEET_NAME  # noqa
from functools import wraps


def create_output_folder(func):
    """There is a decorator, it is used to create the final folder
    and place the file in it
    :param func: function on which the add-in will be performed
    :return: wrapper
    """
    @wraps(func)
    def wrapper(data, name, headings, column_width):
        FILENAME = SPREADSHEET_NAME + ".xlsx"
        if os.path.isdir("../" + RESULT_FOLDER):
            func(data, name, headings, column_width)
        else:
            os.mkdir("../" + RESULT_FOLDER)
            func(data, name, headings, column_width)
        shutil.copy(FILENAME, "../" + RESULT_FOLDER)
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
    return wrapper
