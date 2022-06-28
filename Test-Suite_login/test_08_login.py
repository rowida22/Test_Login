"""Passing valid phone and password
 TC_08_LOGIN Refer to https://sampletestcases.com/test-cases-for-fb-login-page/ """

from asyncio.log import logger
from packages.logger import project_logger
from packages.testsuites.suite_login.init import (
    TestData, SetUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 8")

class test_08_login(unittest.TestCase): # pylint: disable=too-many-instance-attributes
    """Passing valid phone and password"""

    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        SetUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_08(self):
        """Passing valid phone and password"""
        self.email.send_keys(  # pylint: disable=no-member
            self.testdata.PHONE_VALID)
        self.password.send_keys(  # pylint: disable=no-member
            self.testdata.PASSWORD_VALID)
        self.login.click()  # pylint: disable=no-member
        self.assertTrue(self.classifier.find_text_field_matching_label(# pylint: disable=no-member
            "blank").is_displayed(), "Password is required")

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_08_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)