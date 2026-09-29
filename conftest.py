import os
import tempfile
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()

    # Set HEADLESS from env (default: false)
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    if headless:
        chrome_options.add_argument("--headless=new")  # For Chrome v109+
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    # ✅ Create a temporary, unique user data dir
    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    # Optional (safe prefs)
    chrome_options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
    })

    # Create driver

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
