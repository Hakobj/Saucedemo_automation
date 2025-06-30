from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..utils.load_config import load_user_and_pass


config = load_user_and_pass()
USERNAME = config["username"]
PASSWORD = config["password"]


class LoginPage(BasePage):
    CURRENT_URL = config["base_url"]
    USERNAME_SELECTOR = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_SELECTOR = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN_SELECTOR = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.enter_text(self.USERNAME_SELECTOR, USERNAME)
        self.enter_text(self.PASSWORD_SELECTOR, PASSWORD)
        self.click(self.LOGIN_BTN_SELECTOR)



