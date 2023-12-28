from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.test_status import TestStatus


import time
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)



    @pytest.mark.run(order=2)
    def test_validLogin(self):
        time.sleep(10)                  # Finally worked after i added in sleep and self.lp.logout()
        self.lp.logout()
        self.lp.login("test@email.com","abcabc")
        result1 = self.lp.verifyTitle()
        # assert result1 == True
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        # assert result2 == True
        self.ts.markFinal("test_validLogin", result2, "Login Verification")

        #self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
            #self.driver.get(self.baseURL)
            self.lp.logout()
            self.lp.login("teammate@email.com", "abcabcabc")
            result = self.lp.verifyLoginFailed()

            assert result == True




        # userIcon = driver.find_element(By.ID, "dropdownMenu1")
        # if userIcon is not None:
        #     print("Login Successful")
        # else:
        #     print("Login Failed")

    # baseURL = "https://www.letskodeit.com/"
    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    # driver.get(baseURL)

    # lp = LoginPage(self.driver)

#ff = LoginTests()
#ff.test_validLogin()