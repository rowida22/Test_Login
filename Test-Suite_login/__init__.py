"""Base for testsuites."""

import time

from packages.logger import project_logger
from packages.classifier import ClassifierClient as classifier_client_python
from packages.testlink import get_link_to_test_without_validate
from packages.project_selenium import (setup_selenium_driver, teardown_selenium_driver,
                                       webdriver, selenium_exceptions,
                                       By, EC, WebDriverWait, unittest)

logger = project_logger("Registration Test Suite initialization")

class TestData:
    """test data that is used in the test cases"""
    logger.info("initializing test data")
    BLANK_SPACES = " "
    PASSWORD_NUM = "12345678"
    PASSWORD_VALID = "12345678eer"
    PASSWORD_LETTER = "Password"
    PASSWORD_NUM_LETTER = "Pass123456"
    EMAIL_VALID = "test7@gmail.com"
    EMAIL_INVALID = "test@gmail.com"
    EMAIL_INVALID2 = "test.22@gmail.com"
    EMAIL_NUM = "01213344422"
    EMAIL_WITHOUT_AT = "testgmail.com"
    EMAIL_AT_IN_WORD = "testAtgmail.com"
    EMAIL_WITHOUT_DOT = "test@gmailcom"
    RANDOM = "sjanfljbaoubl"


class SetUp:  # pylint: disable = too-few-public-methods, too-many-instance-attributes
    """called before every test"""

    def __init__(self, driver):
        try:
            logger.info("setting up the test")
            self.classifier = classifier_client_python(driver)
            driver.implicitly_wait(5)
            driver.get(get_link_to_test_without_validate())

        except Exception as ex:
            logger.error("test data initialization failed")
            logger.error(ex)
            logger.error(ex.__doc__)
            raise Exception(
                f"test data initialization failed. {ex.__doc__}") from ex

class TearDown():  # pylint: disable = too-few-public-methods
    """called after every test"""

    def __init__(self, driver):
        try:
            logger.info("Tearing down Registration Test Suite")
            logger.info("tearing down the test")
            teardown_selenium_driver(driver)
            logger.info("test tear down")
        except Exception as ex:
            logger.error("test data initialization failed")
            logger.error(ex)
            logger.error(ex.__doc__)
            raise Exception(
                f"test data initialization failed. {ex.__doc__}") from ex

__all__ = ["SetUp", "TearDown", "webdriver", "selenium_exceptions", "By", "EC", "WebDriverWait",
           "unittest", "project_logger", "classifier_client_python",
           "get_link_to_test_without_validate", "setup_selenium_driver"]
__author__ = "Rowida Muhammad"
__license__ = "MIT"
__email__ = "rowida91200@gmail.com"