"""
Author: Abdullah Al Faroque, Date: May 12, 2023
"""
import datetime
from pathlib import Path

from Resources.ExcelUtils import *


class ApplicationSettings:
    """
    This class is used to store the application settings.
    """

    file_ext = ".exe"
    browser_name = "chrome"
    image_folder_path = None
    start_time = datetime.datetime.now()
    excel_path = Path(__file__).resolve().parent.parent / "Test/TestData/test_data.xlsx"
    # Environment details
    url = ""
    test_data_file_path = excel_path

    def setUp(self, os="win"):
        data = read_configuration_data_from_excel(
            ApplicationSettings.test_data_file_path, sheet_name="configuration"
        )

        if os is not None and os.lower() == "win":
            self.file_ext = ".exe"
        else:
            self.file_ext = ""

        self.browser_name = data["browser"]
        self.url = data["frontend_url"]

    def get_test_data_from_excel(self, sheet_name, table_name):
        """
        returns the test data from excel sheet based on the table name
        :param sheet_name:
        :param table_name:
        :return:
        """
        return read_data_from_excel_by_row(
            self.test_data_file_path, sheet_name, table_name
        )

    def set_browser_name(self, browser_name):
        self.browser_name = browser_name

    def set_url(self, url):
        self.url = url

    def set_image_folder_path(self, image_folder_path):
        self.image_folder_path = image_folder_path

    def get_browser_name(self):
        return self.browser_name.lower()

    def get_test_url(self):
        return self.url

    def get_image_folder_path(self):
        return self.image_folder_path

    def get_start_time(self):
        return self.start_time

    def get_file_ext(self):
        return self.file_ext

    @staticmethod
    def get_login_credentials_table_name():
        return "login_test"

    @classmethod
    def get_signup_data_table_name(cls):
        return "signup"

    def get_test_data_file_path(self):
        """
        returns current test data file path
        :return:
        """
        return self.test_data_file_path

    def get_test_data_file(self):
        """
        returns current test data file path
        :return:
        """
        return "./Test/TestData/test_data.xlsx"
