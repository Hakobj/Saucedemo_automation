from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutCompletePage(BasePage):
    CHECKOUT_COMPLETE_SELECTOR = (By.CSS_SELECTOR, ".title")

    def __init__(self, driver):
        super().__init__(driver)

