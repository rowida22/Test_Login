"""Passing valid phone number and vaild password
 TC_03_LOGIN 
 Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuits.suite_login_init import(
    TestData, setUp, TearDown, setup_selenium_driver,unittest)

logger = project_logger("Login Test Case 3")

class test_03_login(unittest.TestCase):
    """Passing invalid phone number and valid password"""
    def setUp(self):
        """Called before every test"""
        self.driver = setup_selenium_driver()
        setUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_03(self):
        """Passing invalid phone number and valid password"""
        self.email.send_keys(
            self.testdata.EMAIL_NUM)
        self.password.send_keys(
            self.testdata.PASSWORD_NUM)
        self.login.click()
        #MISS
        incorrect = "should enter to home page"
    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_03_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)     