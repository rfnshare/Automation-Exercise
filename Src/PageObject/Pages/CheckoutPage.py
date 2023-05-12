import time
from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import CheckoutPageLocators
from Test.TestData.AllTestData import MyData


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = CheckoutPageLocators

    def verify_address_details(self):
        self.wait_till_presence_of_element_located(10, self.locator.CHECKOUT_INFORMATION_BOX)
        self.assert_element_text(True, "Mr. " + MyData.NAME, self.locator.FULL_NAME)
        self.assert_element_text(True, MyData.COMPANY, self.locator.COMPANY_NAME)
        self.assert_element_text(True, MyData.ADDRESS, self.locator.ADDRESS_NAME)
        self.assert_element_text(True, MyData.MOBILE_NUMBER, self.locator.MOBILE_NUMBER_NAME)

    def review_and_place_order(self):
        self.scroll_down()
        self.type_text(self.locator.COMMENT_BOX, MyData.COMMENT)
        self.click(self.locator.PLACE_ORDER_BUTTON)
