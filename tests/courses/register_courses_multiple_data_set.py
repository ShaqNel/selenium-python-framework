from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.test_status import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("Selenium WebDriver 4 with Python", "4242424242424242", "1231", "999"), ("JavaScript", "4242424242424242", "1231", "888"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.clickAllCoursesLink()
        self.courses.enterCourseName(courseName)
        self.courses.clickSearchButton()
        time.sleep(2)
        self.courses.selectFromAllCoursesToEnroll(courseName)
        self.courses.clickCourseEnrollButton()
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        self.courses.clickAllCoursesLink()
        # self.driver.find_element_by_link_text("All Courses").click()
        # self.driver.find_element_by_xpath("//a[@class='navbar-brand header-logo']").click()
        # self.driver.get("https://learn.letskodeit.com/courses")