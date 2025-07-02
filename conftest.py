import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Setup
    chrome_options = Options()
    # chrome_options.add_experimental_option("prefs", {
    #     "profile.password_manager_leak_detection": False
    # })

    driver = webdriver.Chrome(options=chrome_options)
    yield driver

    # Teardown
    driver.quit()
