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
    PROCEED_TO_CHECKOUT = (By.XPATH, "//a[contains(@class,'check_out')]")
    REGISTER_LOGIN = (By.XPATH, "//u[contains(text(),'Register')]")


class LoginRegistrationPageLocators:
    NAME = (By.XPATH, "//input[@name='name']")
    EMAIL = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[text()='Signup']")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login-form")
    TITLE = (By.ID, "id_gender1")
    PASSWORD = (By.ID, "password")

    DAY = (By.ID, "days")
    MONTH = (By.ID, "months")
    YEAR = (By.ID, "years")

    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    COMPANY = (By.ID, "company")
    ADDRESS = (By.ID, "address1")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Create Account')]")
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//h2[@data-qa='account-created']")
    CONTINUE = (By.XPATH, "//a[@data-qa='continue-button']")
    USER_NAME = (By.TAG_NAME, "b")
    GOOGLE_AD = (By.ID, "dismiss-button")


class CheckoutPageLocators:
    CHECKOUT_INFORMATION_BOX = (By.CSS_SELECTOR, ".checkout-information")
    FULL_NAME = (By.XPATH, "(//li[contains(@class, 'address_firstname')])[1]")
    COMPANY_NAME = (By.XPATH, "(//li[contains(@class, 'address_address1')])[1]")
    ADDRESS_NAME = (By.XPATH, "(//li[contains(@class, 'address_address1')])[2]")
    MOBILE_NUMBER_NAME = (By.XPATH, "(//li[contains(@class, 'address_phone')])[1]")

    COMMENT_BOX = (By.TAG_NAME, "textarea")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[text()='Place Order']")


class PaymentPageLocators:
    PAYMENT_INFORMATION_BOX = (By.CSS_SELECTOR, ".payment-information")
    CARD_NAME = (By.XPATH, "//input[@name='name_on_card']")
    CARD_NUMBER = (By.XPATH, "//input[@name='card_number']")
    CVC = (By.XPATH, "//input[@name='cvc']")
    EXPIRATION_MONTH = (By.XPATH, "//input[@name='expiry_month']")
    EXPIRATION_YEAR = (By.XPATH, "//input[@name='expiry_year']")

    CONFIRM_ORDER_BUTTON = (By.ID, "submit")

    ORDER_SUCCESS = (By.XPATH, "(//div[contains(@class, 'alert-success')])[1]")
