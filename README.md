# Saucedemo Automation Test Suite

This project contains end-to-end UI tests for https://www.saucedemo.com using:

- 🐍 Python
- 💡 Selenium WebDriver
- 🧪 Pytest
- 📄 HTML Reports via `pytest-html`
- 🧱 Page Object Model (POM) structure

---

### 📁 Project Structure

```
Saucedemo_automation/
├── conftest.py                # Pytest fixtures (e.g., driver setup)
├── pages/                     # Page Object classes
│   ├── __init__.py
│   ├── base_page.py           # Contains bas page class
│   └── login_page.py          # Contains login page class 
├── tests/                     # Test cases
│   ├── __init__.py
│   └── test_login.py          # Contains login page test 
├── config/
│   └── config.json            # Optional test credentials/config
|── utils/
|   ├── __init__.py
│   ├── load_config.py         # Loading credentials
    
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourname/saucedemo-automation.git
cd saucedemo-automation
```

### 2. Install dependencies
```pip install -r requirements.txt```


### 3. Running tests:
```
pytest .\tests\ # all tests
pytest .\tests\test_login.py # login test
```

### 3. Running tests with HTML report:
```
pytest .\tests\test_login.py --html=report.html
```
