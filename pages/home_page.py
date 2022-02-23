from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.search_result_page import SearchResultPage


class HomePage(BasePage):

    SEARCH_BAR_XPATH = "//form[@role='search']"
    SEARCH_BAR = (By.XPATH, SEARCH_BAR_XPATH)
    SEARCH_INPUT = (By.XPATH, "//input[@name='q']")
    SEARCH_FIRST_SUGGESTION = (By.XPATH, SEARCH_BAR_XPATH + "//li[1]//div")

    def gotoHomePage(self):
        self._driver.get(self._config[self.KV_BASE_URL])

    def __init__(self, config):
        super().__init__(config)
        self.gotoHomePage()

    def is_search_bar_dislayed(self):
        return self.find(self.SEARCH_BAR).is_displayed()

    def type(self, text):
        self.find(self.SEARCH_INPUT).send_keys(text)

    def submit(self):
        self.find(self.SEARCH_INPUT).submit()
        return SearchResultPage(self._config, self._driver)

    def click_to_search(self):
        #Clicking on the search image will not do anything...
        #Need to choose the first option from the suggested options and click
        self.find(self.SEARCH_FIRST_SUGGESTION).click()
        return SearchResultPage(self._config, self._driver)

