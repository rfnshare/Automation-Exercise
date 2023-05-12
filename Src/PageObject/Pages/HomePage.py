import time

from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = HomePageLocators

    def check_home_page_elements(self):
        """
        This method checks if all the elements on the home page are visible successfully
        :return:
        """
        tests = [self.find_element(*self.locator.NAVBAR), self.find_element(*self.locator.SLIDER)]
        return all(tests)

    def add_products_to_cart(self):
        self.scroll_to_web_element(self.locator.GOOGLE_ADS)
        self.click(self.locator.PRODUCT)
        self.wait_for_clickable_an_element(self.locator.CONTINUE_SHOPPING)
        self.click(self.locator.CONTINUE_SHOPPING)
        # self.click(self.locator.SCROLL_UP)
        self.scroll_up()

    def got_to_cart_page(self):
        self.wait_for_clickable_an_element(self.locator.CART)
        self.click(self.locator.CART)
