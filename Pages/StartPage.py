from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class StartPage(BasePage):

    """By locators - OR"""

    FIELD_SEARCH = (By.NAME, "text")
    BUTTON_SEARCH = (By.CLASS_NAME, "a4ai")

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """page actions"""

    def do_search(self, text):
        self.do_send_keys(self.FIELD_SEARCH, text)
        self.do_click(self.BUTTON_SEARCH)

