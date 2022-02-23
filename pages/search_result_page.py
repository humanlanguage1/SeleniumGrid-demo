from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultPage(BasePage):

    SEARCH_BTN = (By.XPATH, "//button[@type='submit']")
    SEARCH_RESULT_DIV_XPATH = "//div[@id='search']"
    SEARCH_RESULT_DIV = (By.XPATH, SEARCH_RESULT_DIV_XPATH)
    SEARCH_RESULTS = (By.XPATH, SEARCH_RESULT_DIV_XPATH + "//div[@class='g']")

    def get_result_count(self):
        try:
            #https://stackoverflow.com/questions/60395570/invalidargumentexception-message-invalid-argument-using-must-be-a-string
            results = self._driver.find_elements(*self.SEARCH_RESULTS)
            return len(results)
        except NoSuchElementException:
            return 0