from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECond

"""This class is the parent of all pages"""
"""It contains all the generic methods and utilities for all pages"""

class BasePage:

    KV_HUB_URL = "Selenium_Grid_Hub"
    KV_PLATFORM = "Platform"
    KV_BROWSER = "Browser"
    KV_BASE_URL = "Base_Url"
    KV_ELEMENT_LOAD_SECONDS = "Element_Load_Seconds"

    #https://www.geeksforgeeks.org/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python/
    #https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.desired_capabilities.html
    """If the page is passed with the driver, config, save the info."""
    """args[0] should always be the config, args[1] can be the driver"""
    """If the driver isn't available, set up a new web driver """
    def __init__(self, *args):
        self._config = args[0]

        if (len(args) == 2):
            self._driver = args[1]
        else:
            capabilities = DesiredCapabilities()
            if self._config[self.KV_BROWSER] == "CHROME":
                capabilities = DesiredCapabilities.CHROME.copy()
            elif self._config[self.KV_BROWSER] == "FIREFOX":
                capabilities.FIREFOX = DesiredCapabilities.FIREFOX.copy()
            capabilities['platform'] = self._config[self.KV_PLATFORM]
            self._driver = webdriver.Remote(
                desired_capabilities=capabilities,
                command_executor=self._config[self.KV_HUB_URL])

    def close(self):
        self._driver.close()

    def wait(self):
        return WebDriverWait(self._driver, self._config[BasePage.KV_ELEMENT_LOAD_SECONDS])

    def find(self, by_locator):
        return self.wait().until(ECond.visibility_of_element_located(by_locator))
