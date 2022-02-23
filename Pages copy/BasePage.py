from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import configReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def getText(self, locator):
        if str(locator).endswith("_XPATH"):
            var = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_CSS"):
            var = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ID"):
            var = self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).text

        return var

    def element(self, locator):
        if str(locator).endswith("_XPATH"):
            return self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            return self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            return self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

    def sendText(self, locator):
        if str(locator).endswith("_XPATH"):
            return self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_text()
        elif str(locator).endswith("_CSS"):
            return self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).send_text()
        elif str(locator).endswith("_ID"):
            return self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_text()

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()

    def send_value(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)