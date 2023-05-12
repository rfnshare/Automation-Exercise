import time

from Src.PageObject.Pages.BasePage import BasePage
from Src.PageObject.Locators import LoginRegistrationPageLocators
from Test.TestData.AllTestData import MyData


class LoginRegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = LoginRegistrationPageLocators

    def user_signup(self):
        self.type_text(self.locator.NAME, MyData.NAME)
        self.type_text(self.locator.EMAIL, MyData.EMAIL)
        self.click(self.locator.SIGNUP_BUTTON)
        self.wait_for_clickable_an_element(self.locator.LOGIN_FORM)
        self.click(self.locator.TITLE)
        self.type_text(self.locator.PASSWORD, MyData.PASSWORD)
        self.select_by_visible_text("16", self.locator.DAY)
        self.select_by_visible_text("June", self.locator.MONTH)
        self.select_by_visible_text("1996", self.locator.YEAR)
        self.type_text(self.locator.FIRST_NAME, MyData.FIRST_NAME)
        self.type_text(self.locator.LAST_NAME, MyData.LAST_NAME)
        self.type_text(self.locator.COMPANY, MyData.COMPANY)
        self.type_text(self.locator.ADDRESS, MyData.ADDRESS)
        self.type_text(self.locator.STATE, MyData.STATE)
        self.type_text(self.locator.CITY, MyData.CITY)
        self.type_text(self.locator.ZIPCODE, MyData.ZIPCODE)
        self.type_text(self.locator.MOBILE_NUMBER, MyData.MOBILE_NUMBER)
        self.click(self.locator.CREATE_ACCOUNT_BUTTON)

    def verify_account_created(self):
        self.wait_till_presence_of_element_located(10, self.locator.ACCOUNT_CREATED_TEXT)
        self.assert_element_text(True, "ACCOUNT CREATED!", self.locator.ACCOUNT_CREATED_TEXT)
        self.click(self.locator.CONTINUE)

    def verify_logged_in_as_username(self):
        self.wait_till_presence_of_element_located(10, self.locator.USER_NAME)
        self.assert_element_text(True, MyData.NAME, self.locator.USER_NAME)
