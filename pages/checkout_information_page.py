from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutInformationCardPage(BasePage):
    TITLE_SELECTOR = (By.CSS_SELECTOR, ".title")
    FIRST_NAME_SELECTOR = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_SELECTOR = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_SELECTOR = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BUTTON_SELECTOR = (By.CSS_SELECTOR, "#continue")

    def __init__(self, driver):
        super().__init__(driver)

    def information_filling(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME_SELECTOR, first_name)
        self.enter_text(self.LAST_NAME_SELECTOR, last_name)
        self.enter_text(self.POSTAL_CODE_SELECTOR, postal_code)
        self.click(self.CONTINUE_BUTTON_SELECTOR)
