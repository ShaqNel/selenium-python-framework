import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _logo_top_link = "//div[@class='navbar-header']//a[@class='navbar-brand navbar-logo text-blue']"
    _home_top_link = "//div[@id='navbar-inverse-collapse']//a[@href='/home']"
    _all_courses_top_link = "//div[@id='navbar-inverse-collapse']//a[@href= '/courses']"
    _interview_top_link = "//div[@id='navbar-inverse-collapse']//a[@href='/interview']"
    _support_top_link = "//div[@id='navbar-inverse-collapse']//a[@href='/support']"
    _blog_top_link = "//div[@id='navbar-inverse-collapse']//a[@href='/blog']"
    _practice_top_link = "//div[@class='dropdown']//a[@class='dynamic-link dropdown-toggle']"
    _my_courses_top_link = "//div[@id='navbar-inverse-collapse']//a[@href='/mycourses']"
    _community_top_link = "//div[@id='navbar-inverse-collapse']//a[@href='/community']"
    _notification_top_link = "//div[@class='zen-notification-menu']"
    _user_settings_icon = "dropdownMenu1"


    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses_top_link, locatorType="xpath")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses_top_link, locatorType="xpath")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice_top_link, locatorType="xpath")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                      locatorType="id", pollFrequency=1)
        self.elementClick(element=userSettingsElement)
        # self.elementClick(locator=self._user_settings_icon,
        #                               locatorType="id")