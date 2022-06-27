"""Passing valid email and password
 TC_02_LOGIN 
 Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuits.suite_login.init import(
    TestData, setUp, TearDown, setup_selenium_driver, unittest)

logger = project_logger("Login Test Case 1")

class test_01_login(unittest.Testcase):
    """Passing valid email and password"""

    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        setUp(self,self.driver)
        self.testdata = TestData()
        logger.info("Setting up the test")

    def test_01(self):
        """Passing vaild email and password"""
        self.email.send_keys(
            self.testdata.EMAIL_VALID)
        self.password.send_keys(
            self.testdata.PASSWORD_LETTER)
        self.login.click()
        #MISS
        corret = "Should enter to home page"

    def tearDown(self):
        """Called after every test"""
        TearDown(self.driver)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_01_login))
    runner = unittest.TextTestRunner
    runner.run(suite)

