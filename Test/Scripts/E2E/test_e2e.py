import allure
import pytest

from Src.PageObject.Pages.HomePage import HomePage
from Src.PageObject.Pages.CartPage import CartPage
from Src.PageObject.Pages.Login_RegistrationPage import LoginRegistrationPage
from Src.TestBase.WebDriverSetup import WebDriverSetup


@allure.title("End To End Test")
@allure.description("Checking product order placed successfully")
class TestHomePage(WebDriverSetup):
    @pytest.mark.smoke
    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        url = home_page.get_url()
        print("Starting to check are all homepage elements visible properly")
        assert (
                home_page.check_home_page_elements() is True
        ), "Home page elements are not visible properly"
        log.info(f"URL {url} is loaded")

        home_page.add_products_to_cart()
        home_page.got_to_cart_page()
        cart_page = CartPage(self.driver)
        cart_page.verify_cart_page_is_displayed()
        log.info(f"Verified that cart page is displayed")

        cart_page.go_to_checkout_page()
        cart_page.go_to_login_registration_page()

        registration = LoginRegistrationPage(self.driver)
        registration.user_signup()
        registration.verify_account_created()
        log.info(f"Verified ACCOUNT CREATED!")
        registration.verify_logged_in_as_username()
        log.info("Verified Logged in as username")
