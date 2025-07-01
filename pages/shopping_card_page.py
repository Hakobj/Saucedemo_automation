from selenium.webdriver.common.by import By
from .base_page import BasePage


class ShoppingCardPage(BasePage):
    CHECKOUT_SELECTOR = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def checkout(self):
        checkout_btn = self.driver.find_element(*self.CHECKOUT_SELECTOR)
        self.click(checkout_btn)