import time
from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import PaymentPageLocators
from Test.TestData.AllTestData import MyData


class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = PaymentPageLocators

    def fill_up_payment_details_and_confirm(self):
        self.wait_till_presence_of_element_located(10, self.locator.PAYMENT_INFORMATION_BOX)
        self.type_text(self.locator.CARD_NAME, MyData.CARD_NAME)
        self.type_text(self.locator.CARD_NUMBER, MyData.CARD_NUMBER)
        self.type_text(self.locator.CVC, MyData.CVC)
        self.type_text(self.locator.EXPIRATION_MONTH, MyData.EXPIRATION_MONTH)
        self.type_text(self.locator.EXPIRATION_YEAR, MyData.EXPIRATION_YEAR)
        self.click(self.locator.CONFIRM_ORDER_BUTTON)

    def verify_successful_order_placed(self):
        self.wait_till_presence_of_element_located(10, self.locator.ORDER_SUCCESS)
        self.assert_element_text_in(True, MyData.ORDER_SUCCESS_MESSAGE, self.locator.ORDER_SUCCESS)


