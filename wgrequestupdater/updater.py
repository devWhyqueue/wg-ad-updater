import logging

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

log = logging.getLogger(__name__)


class WgRequestUpdater:
    WG_REQUEST_URL = "https://www.wg-gesucht.de/gesuch-bearbeiten.html?action=update_request&request_id=9060658"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def update(self, username: str, password: str):
        self.driver.get(WgRequestUpdater.WG_REQUEST_URL)
        self._cookie_consent()
        self._login(username, password)
        self.driver.find_element(By.ID, "update_request").click()
        log.info("WG Request successfully updated.")

    def _cookie_consent(self):
        try:
            WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#cmpwelcomebtnyes > a")))
            self.driver.find_element(By.CSS_SELECTOR, "#cmpwelcomebtnyes > a").click()
        except TimeoutException:
            # No cookie consent necessary
            pass

    def _login(self, username: str, password: str):
        try:
            self.driver.find_element(By.CSS_SELECTOR,
                                     "#headbar_wrapper > div.col-sm-8.noprint > a:nth-child(3)").click()
            self.driver.find_element(By.NAME, "login_email_username").send_keys(username)
            self.driver.find_element(By.NAME, "login_password").send_keys(password)
            self.driver.find_element(By.ID, "login_submit").click()
        except NoSuchElementException:
            # No login button present, so user is already logged in
            pass
