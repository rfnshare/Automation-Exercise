import allure
import pytest

from Src.PageObject.Pages.HomePage import HomePage
from Src.TestBase.WebDriverSetup import WebDriverSetup


@allure.title("End To End Test")
@allure.description("Checking product order placed successfully")
class TestHomePage(WebDriverSetup):
    @pytest.mark.smoke
    def test_01_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        url = home_page.get_url()
        print("Starting to check are all homepage elements visible properly")
        assert (
            home_page.check_home_page_elements() is True
        ), "Home page elements are not visible properly"
        log.info(f"URL {url} is loaded")