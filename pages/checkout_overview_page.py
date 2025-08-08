from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutOverviewPage(BasePage):
    CHECKOUT_OVERVIEW_SELECTOR = (By.CSS_SELECTOR, ".title")
    FINISH_BUTTON_SELECTOR = (By.CSS_SELECTOR, "#finish")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_finish_button(self):
        self.click(self.FINISH_BUTTON_SELECTOR)
