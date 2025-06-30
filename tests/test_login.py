from ..pages.login_page import LoginPage
from ..pages.home_page import HomePage


def test_login_(driver):
    driver.get(LoginPage.CURRENT_URL)
    login_page_obj = LoginPage(driver)
    home_page_obj = HomePage(driver)

    login_page_obj.login()
    home_page_text = home_page_obj.get_text(home_page_obj.HOMEPAGE_TITLE_SELECTOR)

    assert "Products" in home_page_text, "You are not on Home page!!!"
