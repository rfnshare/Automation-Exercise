import string
import random


class MyData:
    email = ''.join(random.choices(string.ascii_uppercase +
                                   string.digits, k=7))
    NAME = "Test Name"
    EMAIL = f"{email}@gmail.com"
    PASSWORD = "Lqa@FiB9tNAJj"

    FIRST_NAME = "Test"
    LAST_NAME = "Name"
    COMPANY = "Kineatik"
    ADDRESS = "Dhaka, Bangladesh"
    STATE = "Dhaka"
    CITY = "Dhaka"
    ZIPCODE = "1201"
    MOBILE_NUMBER = "01879878987"

    COMMENT = "Test Comment"

    CARD_NAME = "Test Card Name"
    CARD_NUMBER = "4485699338868909"
    CVC = "359"
    EXPIRATION_MONTH = "10"
    EXPIRATION_YEAR = "2026"

    ORDER_SUCCESS_MESSAGE = "Your order has been placed successfully!"
