import time

from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = CartPageLocators

    def verify_cart_page_is_displayed(self):
        self.assert_element_is_displayed(self.locator.CART_INFO_TABLE)

    def go_to_checkout_page(self):
        self.click(self.locator.PROCEED_TO_CHECKOUT)

    def go_to_login_registration_page(self):
        self.wait_for_clickable_an_element(self.locator.REGISTER_LOGIN)
        self.click(self.locator.REGISTER_LOGIN)
