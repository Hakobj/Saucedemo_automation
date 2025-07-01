from selenium.webdriver.common.by import By
from .base_page import BasePage


class HomePage(BasePage):
    HOMEPAGE_TITLE_SELECTOR = (By.CSS_SELECTOR, ".title")
    BAG_SELECTOR = (By.CSS_SELECTOR, ".inventory_item_name")

    def __init__(self, driver):
        super().__init__(driver)

    def select_bag(self):
        backpack_items = self.driver.find_elements(*self.BAG_SELECTOR)
        bag = backpack_items[0]
        bag.click()
