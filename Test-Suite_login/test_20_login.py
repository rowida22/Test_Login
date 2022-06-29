""" Verify that if the user clicks on the forgotten password link then
the user should be navigated to the forgot password page.
 TC_20_LOGIN Refer to  https://sampletestcases.com/test-cases-for-fb-login-page/ """

from packages.logger import project_logger
from packages.testsuits.suite_login_init import(
    TestData, setUp, TearDown, setup_selenium_driver,unittest)

logger = project_logger("Login Test Case 20")

class test_20_login(unittest.TestCase):
    """ Verify that if the user clicks on the forgotten password link then 
    the user should be navigated to the forgot password page."""
    
    def setUp(self):
        """called before every test"""
        self.driver = setup_selenium_driver()
        setUp(self, self.driver)
        self.testdata = TestData()
        logger.info("setting up the test")

    def test_20(self):
        """ Verify that if the user clicks on the forgotten password link then 
        the user should be navigated to the forgot password page."""
        self.forgot_password.click()  # pylint: disable=no-member
        self.assertTrue(self.email.is_displayed(), "Email field is not displayed")
        self.assertTrue(self.password.is_displayed(), "Password field is not displayed")

    def tearDown(self):
        """called after every test"""
        TearDown(self.driver)
    
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_20_login))
    runner = unittest.TextTestRunner()
    runner.run(suite)