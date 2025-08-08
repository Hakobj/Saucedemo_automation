from selenium.webdriver.common.by import By
from .base_page import BasePage


class BagPage(BasePage):
    BACK_TO_PRODUCT_SELECTOR = (By.CSS_SELECTOR, "#back-to-products")
    ADD_TO_CARD_SELECTOR = (By.CSS_SELECTOR, "#add-to-cart")
    REMOVE_BUTTON_SELECTOR = (By.CSS_SELECTOR, "#remove")
    SHOPPING_CARD_SELECTOR = (By.CSS_SELECTOR, ".shopping_cart_link")


    def __init__(self, driver):
        super().__init__(driver)

    def add_bag_into_card(self):
        backpack_items = self.driver.find_elements(*self.ADD_TO_CARD_SELECTOR)[0]
        self.click(backpack_items)

    def go_to_shopping_card(self):
        self.click(self.driver.find_element(*self.SHOPPING_CARD_SELECTOR))
