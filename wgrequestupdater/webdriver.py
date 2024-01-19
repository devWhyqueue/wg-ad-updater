from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


def web_driver(exec_path: str = None) -> WebDriver:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")  # Adjusting for Chromium

    if exec_path:
        service = Service(exec_path)
        driver = webdriver.Chrome(service=service, options=options)
    else:
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(3)
    return driver
