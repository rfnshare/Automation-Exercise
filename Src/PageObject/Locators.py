from selenium.webdriver.common.by import By


class HomePageLocators:
    # Home Dashboard Page
    SLIDER = (By.ID, "slider-carousel")
    NAVBAR = (By.XPATH, "//ul[contains(@class,'navbar-nav')]")
    RECOMMENDED_ITEMS = (By.XPATH, "//div[@class='recommended_items']")
    PRODUCT = (By.XPATH, "//div[@class='recommended_items']//div[@class='item active']//a")
    CONTINUE_SHOPPING = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")
    FOOTER = (By.ID, "footer")
    GOOGLE_ADS = (By.XPATH, "(//div[@class='google-auto-placed'])[4]")
    SCROLL_UP = (By.ID, "scrollUp")
    CART = (By.PARTIAL_LINK_TEXT, "Cart")


class CartPageLocators:
    CART_INFO_TABLE = (By.ID, "cart_info_table")


class CheckoutPageLocators:
    pass


class LoginRegistrationPageLocators:
    pass


class PaymentPageLocators:
    pass
