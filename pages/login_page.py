from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..utils.load_config import load_data


config = load_data()
USERNAME = config["login"]["username"]
PASSWORD = config["login"]["password"]


class LoginPage(BasePage):
    USERNAME_SELECTOR = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_SELECTOR = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN_SELECTOR = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_text(self.USERNAME_SELECTOR, username)
        self.enter_text(self.PASSWORD_SELECTOR, password)
        self.click(self.LOGIN_BTN_SELECTOR)



