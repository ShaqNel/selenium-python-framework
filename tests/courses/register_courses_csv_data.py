from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.test_status import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import time
from pages.home.navigation_page import NavigationPage

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()
    #     self.courses.clickAllCoursesLink()
        # self.driver.find_element_by_link_text("All Courses").click()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/shaquillenelson/Documents/workspace_python/seleniumWD2Tutorial/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.courses.clickAllCoursesLink()
        self.courses.enterCourseName(courseName)
        self.courses.clickSearchButton()
        time.sleep(1)
        self.courses.selectFromAllCoursesToEnroll(courseName)
        self.courses.clickCourseEnrollButton()
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")

        # self.courses.enterCourseName(courseName)
        # time.sleep(1)
        # self.courses.selectCourseToEnroll(courseName)
        # time.sleep(1)
        # self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
        # time.sleep(1)
        # result = self.courses.verifyEnrollFailed()
        # self.ts.markFinal("test_invalidEnrollment", result,
        #                   "Enrollment Failed Verification")