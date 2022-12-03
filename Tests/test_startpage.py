import pytest
import time
from Config.config import TestData
from Pages.StartPage import StartPage
from Tests.test_base import BaseTest


class Test_Search(BaseTest):

    def test_search(self):
        self.startPage = StartPage(self.driver)
        self.startPage.do_search(TestData.TEXT)
        time.sleep(10)

