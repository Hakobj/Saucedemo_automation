from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Instantiation of webdriver
driver = webdriver.Chrome()


def go_to_demo_page():
    driver.get("https://www.saucedemo.com/")


def login(user_name, pswd):
    # Login process
    username = driver.find_element(By.CSS_SELECTOR, "#user-name")
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")

    username.send_keys(user_name)
    password.send_keys(pswd)
    login_button.click()
    time.sleep(2)
    # alert = driver.switch_to.alert
    # alert.accept()
    # assertion


def select_bag():
    # Product details page
    backpack_items = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
    bag = backpack_items[0]
    bag.click()
    # assertion


def add_bag_into_card():
    # Product page
    add_to_card = driver.find_element(By.CSS_SELECTOR, "#add-to-cart")
    add_to_card.click()
    # assertion


def go_to_shopping_card():
    # Shoping card page
    shopping_cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    shopping_cart.click()


def checkout_page():
    # Checkout button
    checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout.click()
    # assertion


def checkout_information_filling(first_name, last_name, postal_code):
    # Checkout information page
    first_name_textbox = driver.find_element(By.CSS_SELECTOR, "#first-name")
    last_name_textbox = driver.find_element(By.CSS_SELECTOR, "#last-name")
    postal_code_textbox = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")

    first_name_textbox.send_keys(first_name)
    last_name_textbox.send_keys(last_name)
    postal_code_textbox.send_keys(postal_code)
    continue_button.click()
    # assertion


def finish():
    finish_button = driver.find_element(By.CSS_SELECTOR, "#finish")
    finish_button.click()
    # assertion


def cleanUp():
    driver.quit()


# Whole process
go_to_demo_page()
time.sleep(2)
login("standard_user", "secret_sauce")
time.sleep(2)
select_bag()
time.sleep(2)
add_bag_into_card()
time.sleep(2)
go_to_shopping_card()
time.sleep(2)
checkout_page()
time.sleep(2)
checkout_information_filling("Hakob", "Julfayan", "0017")
time.sleep(2)
finish()
time.sleep(2)



