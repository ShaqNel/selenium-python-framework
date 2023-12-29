import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests
from tests.home.navigation_test import NavigationTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(NavigationTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)