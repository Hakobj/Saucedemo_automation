from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options


# Adding chrome options to disable Google Password manager popup
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "profile.password_manager_leak_detection": False
})

# Instantiation of webdriver
driver = webdriver.Chrome(options=chrome_options)


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


def test_login():
    assert "Products" in driver.find_element(By.CSS_SELECTOR, ".title").text


def select_bag():
    # Product details page
    backpack_items = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
    bag = backpack_items[0]
    bag.click()


def test_bag_selection():
    assert "Back to products" in driver.find_element(By.CSS_SELECTOR, "#back-to-products").text


def add_bag_into_card():
    # Product page
    add_to_card = driver.find_element(By.CSS_SELECTOR, "#add-to-cart")
    add_to_card.click()


def test_bag_adding():
    assert "Remove" in driver.find_element(By.CSS_SELECTOR, "#remove").text


def go_to_shopping_card():
    # Shopping card page
    shopping_cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    shopping_cart.click()


def test_shopping_card():
    assert "Checkout" in driver.find_element(By.CSS_SELECTOR, "#checkout").text


def checkout_page():
    # Checkout button
    checkout = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout.click()


def test_checkout_page():
    assert "Checkout: Your Information" in driver.find_element(By.CSS_SELECTOR, ".title").text


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


def test_checkout_overview():
    assert "Checkout: Overview" in driver.find_element(By.CSS_SELECTOR, ".title").text


def finish():
    finish_button = driver.find_element(By.CSS_SELECTOR, "#finish")
    finish_button.click()


def test_checkout_complete():
    assert "Checkout: Complete!" in driver.find_element(By.CSS_SELECTOR, ".title").text


def cleanUp():
    driver.quit()


# Whole process
go_to_demo_page()
time.sleep(2)

login("standard_user", "secret_sauce")
time.sleep(2)
test_login()

select_bag()
time.sleep(2)
test_bag_selection()

add_bag_into_card()
time.sleep(2)
test_bag_adding()
time.sleep(2)

go_to_shopping_card()
time.sleep(2)
test_shopping_card()

checkout_page()
time.sleep(2)
test_checkout_page()

checkout_information_filling("Hakob", "Julfayan", "0017")
time.sleep(2)
test_checkout_overview()

finish()
time.sleep(2)
test_checkout_complete()

time.sleep(2)
cleanUp()



