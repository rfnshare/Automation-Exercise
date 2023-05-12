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