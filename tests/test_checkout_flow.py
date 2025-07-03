from ..pages.login_page import LoginPage
from ..pages.home_page import HomePage
from ..pages.bag_page import BagPage
from ..pages.shopping_card_page import ShoppingCardPage
from ..pages.checkout_information_page import CheckoutInformationCardPage
from ..pages.checkout_overview_page import CheckoutOverviewPage
from ..pages.checkout_complete_page import CheckoutCompletePage
from ..utils.load_config import load_data


def test_user_can_login_and_complete_checkout(driver):
    # Instantiate all necessary page objects
    login_page_obj = LoginPage(driver)
    home_page_obj = HomePage(driver)
    bag_page_obj = BagPage(driver)
    shopping_card_page_obj = ShoppingCardPage(driver)
    checkout_information_page_obj = CheckoutInformationCardPage(driver)
    checkout_overview_page_obj = CheckoutOverviewPage(driver)
    checkout_complete_page_obj = CheckoutCompletePage(driver)

    # Test login
    # Load user and pass data, then login
    config = load_data()
    current_url = config["base_url"]
    username = config["login"]["username"]
    password = config["login"]["password"]

    # Open browser, go to website and login
    login_page_obj.open_website(current_url)
    login_page_obj.login(username, password)

    home_page_text = home_page_obj.get_text(home_page_obj.HOMEPAGE_TITLE_SELECTOR)
    expected_text = "Products"
    assert expected_text in home_page_text, f"Expected text is {expected_text}, actual text is {home_page_text}"

    # Test bag item adding
    home_page_obj.select_bag()
    back_to_products_text = bag_page_obj.get_text(bag_page_obj.BACK_TO_PRODUCT_SELECTOR)
    expected_text = "Back to products"
    assert expected_text in back_to_products_text, f"Expected text is {expected_text}, actual text is {back_to_products_text}"

    # Test added bag
    bag_page_obj.add_bag_into_card()
    remove_btn_text = bag_page_obj.get_text(bag_page_obj.REMOVE_BUTTON_SELECTOR)
    expected_text = "Remove"
    assert expected_text in remove_btn_text, f"Expected text is {expected_text}, actual text is {remove_btn_text}"

    # Test shopping card page, checkout button
    bag_page_obj.go_to_shopping_card()
    checkout_btn_text = shopping_card_page_obj.get_text(shopping_card_page_obj.CHECKOUT_SELECTOR)
    expected_text = "Checkout"
    assert expected_text in checkout_btn_text, f"Expected text is {expected_text}, actual text is {checkout_btn_text}"

    # Test checkout
    shopping_card_page_obj.checkout()
    checkout_information_text = checkout_information_page_obj.get_text(checkout_information_page_obj.TITLE_SELECTOR)
    expected_text = "Checkout: Your Information"
    assert expected_text in checkout_information_text, f"Expected text is {expected_text}, actual text is \
    {checkout_information_text}"

    # Test checkout overview
    # Read data
    first_name = config["checkout"]["first_name"]
    last_name = config["checkout"]["last_name"]
    postal_code = config["checkout"]["postal_code"]

    checkout_information_page_obj.information_filling(first_name, last_name, postal_code)
    checkout_overview_text = checkout_overview_page_obj.get_text(checkout_overview_page_obj.CHECKOUT_OVERVIEW_SELECTOR)
    expected_text = "Checkout: Overview"
    assert expected_text in checkout_overview_text, f"Expected text is {expected_text}, actual text is \
    {checkout_overview_text}"

    # Test final page
    checkout_overview_page_obj.click_on_finish_button()
    checkout_complete_text = checkout_complete_page_obj.get_text(checkout_complete_page_obj.CHECKOUT_COMPLETE_SELECTOR)
    expected_text = "Checkout: Complete!"
    assert expected_text in checkout_complete_text, f"Expected text is {expected_text}, actual text is \
    {checkout_complete_text}"
