import platform

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from Utilities import configReader


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome"], scope="class")
def get_browser(request):
    if request.param == "chrome":
        chrome_options = Options()
        prefs = {
            "intl.accept_languages": "en-US"
        }
        chrome_options.add_experimental_option("prefs", prefs)
        if platform.system() == 'Linux':
            driver = webdriver.Remote(command_executor="http://chrome:4444/wd/hub",options=webdriver.ChromeOptions())
        elif platform.system() == 'Windows':
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    request.cls.driver = driver
    driver.get(configReader.readConfig("basic info", "testSiteUrl"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def setup_module(module):
    print("Creating DB Connection")


def setup_function(function):
    print("Launching browser")