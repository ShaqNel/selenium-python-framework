# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.test_status import TestStatus
import unittest
import pytest
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidRedeem(self):
        self.courses.redeemCourse(redeem="ABCDEF",name="Javascript")
        # self.courses.clickAllCoursesLink()
        # self.courses.enterCourseName("Javascript")
        # self.courses.clickSearchButton()
        # time.sleep(2)
        # self.courses.selectCourseToEnroll()
        # self.courses.clickCourseEnrollButton()
        # self.courses.redeemCoupon(redeem="ABCDEF")
        result = self.courses.verifyRedeemFailed()
        self.ts.mark(result, "Redeem Failed Verification")
        # assert result == True
        # self.ts.markFinal("test_invalidRedeem", result1,
        #                   "Redeem Failed Verification")

    @pytest.mark.run(order=2)
    def test_invalidEnroll(self):
        self.courses.enrollCourse(num="4242 4242 4242 4242", exp="1234", cvv="888")
        result2 = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnroll", result2,
                          "Enroll Failed Verification")

        # self.courses.enrollCourse()
        # result = self.courses.verifyEnrollFailed()
        #
        # assert result == True

    # def test_courseSearch(self):
    #     baseURL = "https://www.letskodeit.com/"
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #
    #
    #
    #     driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']//a[@href= '/courses']").click()
    #     driver.find_element(By.XPATH, "//input[@id= 'search']").send_keys("Javascript")
    #     driver.find_element(By.XPATH, "//button[@type= 'submit']").click()
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, "//div[@class= 'zen-course-list']").click()
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, "//button[@class= 'dynamic-button btn btn-default btn-lg btn-enroll']").click()
    #     time.sleep(2)
    #     driver.execute_script("window.scrollBy(0, 1000);")
    #     driver.find_element(By.XPATH, "//a[@class='coupon apply-coupon']").click()
    #     time.sleep(1)
    #     driver.find_element(By.XPATH, "//input[@id='inputSuccess2']").send_keys("ABCDEFG")
    #     time.sleep(1)
    #     driver.find_element(By.XPATH, "//a[@class='dynamic-button btn btn-primary btn-sm4 btn-email-change redeem-coupon']").click()
    #     time.sleep(2)
    #
    #     errorMessage = driver.find_element(By.XPATH, "//div[@class='form-group has-error']//div[@class='message text-danger']")
    #     if errorMessage is not None:
    #         print("Invalid Redeem Test Successful")
    #     else:
    #         print("Invalid Redeem Test Failed")
    #
    #
    #


        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(2)
        # driver.switch_to.frame("__privateStripeFrame1776")
        # time.sleep(5)
        # driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/form[1]/span[2]/div[1]/div[1]/div[2]/span[1]/input[1]").send_keys(4242424242424242)
        # time.sleep(2)
        # # cardNumber = driver.find_element(By.XPATH, "//div[@id='card-number']")
        # # cardNumber.send_keys("4242424242424242")
        # time.sleep(2)
        # # driver.find_element(By.XPATH, "//div[@id='card-number']").send_keys("4242424242424242")
        # # time.sleep(2)
        # driver.find_element(By.XPATH, "//div[@id='card-expiry']").send_keys(1234)
        # time.sleep(1)
        # driver.find_element(By.XPATH, "//div[@id='card-cvc']").send_keys(123)
        # time.sleep(1)
        # driver.find_element(By.XPATH, "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']").click()
        # time.sleep(2)
        #
        #
        # errorMessage = driver.find_element(By.XPATH, "//div[@class='card-errors has-error']")
        # if errorMessage is not None:
        #     print("Invalid Card Test Successful")
        # else:
        #     print("Invalid Card Test Failed")


#         driver.quit()
#
# ff = CoursesTest()
# ff.test_courseSearch()