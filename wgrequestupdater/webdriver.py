from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


def chrome_driver() -> WebDriver:
    options = Options()
    options.headless = True
    options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    return driver
