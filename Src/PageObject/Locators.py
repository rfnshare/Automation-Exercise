from selenium.webdriver.common.by import By


class HomePageLocators:
    # Home Dashboard Page
    SLIDER = (By.ID, "slider-carousel")
    NAVBAR = (By.XPATH, "//ul[contains(@class,'navbar-nav')]")


class CartPageLocators:
    pass


class CheckoutPageLocators:
    pass


class LoginRegistrationPageLocators:
    pass


class PaymentPageLocators:
    pass
