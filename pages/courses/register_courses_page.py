import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "//input[@id= 'search']"
    _search_button = "//button[@type= 'submit']"
    _course = "//div[@class= 'zen-course-list']" # For single course on page or when searching Javascript
    _select_course = "//h4[contains(@class,'dynamic-heading') and contains(text(),'{0}')]"
    _all_courses = "//h4[@class='dynamic-heading']" # When searching Selenium and there are multiple matching nodes on page
    _all_courses_top_link = "//div[@id='navbar-inverse-collapse']//a[@href= '/courses']"
    _enroll_button = "//button[@class= 'dynamic-button btn btn-default btn-lg btn-enroll']"
    _apply_redeem = "//a[@class='coupon apply-coupon']"
    _redeem_box = "//input[@id='inputSuccess2']"
    _submit_redeem = "//a[@class='dynamic-button btn btn-primary btn-sm4 btn-email-change redeem-coupon']"
    _redeem_error_message = "//div[@class='form-group has-error']//div[@class='message text-danger']"
    # NEW TEST LOCATORS ON SAME COURSES PAGE
    _cc_num = "//div[@class='CardNumberField-input-wrapper']//input[@class='InputElement is-empty Input Input--empty']"
    _cc_exp = "//div[@class='SplitCardField is-link-hidden previous-link-hidden']//Input[@autocomplete='cc-exp']"
    _cc_cvv = "//div[@class='SplitCardField is-link-hidden previous-link-hidden']//Input[@autocomplete='cc-csc']"
    _zip = ""
    _agree_to_terms_checkbox = ""
    _enroll_error_message = "//div[@class='card-errors has-error']"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    # /parent::div


    ############################
    ### Element Interactions ###
    ############################
    def clickAllCoursesLink(self):
        self.elementClick(self._all_courses_top_link, locatorType="xpath")

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box, locatorType="xpath")

    def clickSearchButton(self):
        self.elementClick(self._search_button, locatorType="xpath")

    def selectCourseToEnroll(self):
        self.elementClick(locator=self._course, locatorType="xpath")
        # self.elementClick(self._course, locatorType="xpath")

    def selectFromAllCoursesToEnroll(self, fullCourseName):
        self.elementClick(locator=self._all_courses.format(fullCourseName), locatorType="xpath")

    def clickCourseEnrollButton(self):
        self.elementClick(self._enroll_button, locatorType="xpath")

    def clickApplyRedeemCode(self):
        self.elementClick(self._apply_redeem, locatorType="xpath")

    def enterRedeemCode(self, redeem):
        self.sendKeys(redeem, self._redeem_box, locatorType="xpath")

    def clickRedeemSubmitButton(self):
        self.elementClick(self._submit_redeem, locatorType="xpath")

    def redeemCoupon(self, redeem):
        self.clickApplyRedeemCode()
        self.enterRedeemCode(redeem)
        self.clickRedeemSubmitButton()



    def redeemCourse(self, redeem="", name=""):
        self.clickAllCoursesLink()
        self.enterCourseName(name)
        self.clickSearchButton()
        time.sleep(3)
        self.selectCourseToEnroll()
        self.clickCourseEnrollButton()
        self.redeemCoupon(redeem)




    def verifyRedeemFailed(self):
        messageElement = self.waitForElement(self._redeem_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)

        # result = self.isElementPresent(self._redeem_error_message, locatorType="xpath")
        #
        return result



# NEW ENROLL TEST WITH IFRAMES
    def enterCardNum(self, num):
        time.sleep(10)
        # self.switchToFrame(name="__privateStripeFrame4516")
        self.SwitchFrameByIndex(self._cc_num, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_num, locatorType="xpath")
        # self.sendKeys(num, locator=self._cc_num, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        # self.switchToFrame(name="__privateStripeFrame45110")
        # self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        # self.switchToDefaultContent()
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        # self.switchToFrame(name="__privateStripeFrame4518")
        # self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        # self.switchToDefaultContent()
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="xpath")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="xpath")
        self.switchToDefaultContent()

    # def enterZip(self, zip):
    #     self.switchToFrame(name="__privateStripeFrame7")
    #     self.sendKeys(zip, locator=self._zip, locatorType="name")
    #     self.switchToDefaultContent()
    #
    # def clickAgreeToTermsCheckbox(self):
    #     self.elementClick(locator=self._agree_to_terms_checkbox)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        # self.enterZip(zip)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()


    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result

    # The method below is to verify that enroll button is disabled

    # def verifyEnrollFailed(self):
    #     result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
    #                             info="Enroll Button")
    #     return not result


