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

    def get_text(self):
        return self.find_element(*self.locator.NAVBAR).text
