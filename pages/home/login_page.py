import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)

    # Locators
    _login_link = "//div[@id='header5']//div//div//div//div//div//a[@class='dynamic-link']"
    _email_field = "email"
    _password_field = "login-password"
    _login_button = "login"

 #   def getLoginLink(self):
 #       return self.driver.find_element(By.XPATH, self._login_link)

 #    def getEmailField(self):
 #       return self.driver.find_element(By.ID, self._email_field)

 #   def getPasswordField(self):
 #       return self.driver.find_element(By.ID, self._password_field)

 #   def getLoginButton(self):
 #       return self.driver.find_element(By.ID, self._login_button)

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")  #self.getLoginLink().click() no longer needed, se this first then when we refine code no longer needed

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)  #self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field) #self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id") #self.getLoginButton().click()

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    def login(self, email="", password=""):
        self.clickLoginLink()
        time.sleep(2)
        self.clearFields()
        time.sleep(2)
        self.enterEmail(email)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLoginButton()
        time.sleep(2)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("dropdownMenu1", locatorType="id")     #userIcon = driver.find_element(By.ID, "dropdownMenu1")

        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//form[@method='POST']//span[@id='incorrectdetails']", locatorType="xpath")

        return result

    def verifyTitle(self):
        return self.verifyPageTitle("My Courses")
        # if "Google" in self.getTitle():
        #     return True
        # else:
        #     return False

    def logout(self):
        self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="//a[@href='/logout']",
                                      locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
        # time.sleep(2)
        # self.elementClick(locator="//a[@href='/logout']", locatorType="xpath")

#       loginLink = self.driver.find_element(By.XPATH, "//div[@id='header5']//div//div//div//div//div//a[@class='dynamic-link']")
#       loginLink.click()

#        emailField = self.driver.find_element(By.ID, "email")
#        emailField.send_keys(username)

#        passwordField = self.driver.find_element(By.ID, "login-password")
#        passwordField.send_keys(password)

#        loginButton = self.driver.find_element(By.ID, "login")
#        loginButton.click()
