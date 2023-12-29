import unittest
import pytest
from utilities.test_status import TestStatus
from pages.home.navigation_page import NavigationPage
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class NavigationTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.nav = NavigationPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_navigationBar(self):
        self.nav.navBarTest()
        time.sleep(1)
        self.nav.verifyMyAccount()
        time.sleep(2)
        result1 = self.nav.verifyTitle()
        self.ts.markFinal("test_navigationBar", result1, "Title Verification")
