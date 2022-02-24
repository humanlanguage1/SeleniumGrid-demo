import os
import platform
import subprocess
from configparser import ConfigParser
from subprocess import Popen
from time import sleep

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def get_browser(request):
    remote_url = "http://localhost:4444/wd/hub"
    script_name = r"C:\Users\USER\PycharmProjects\PageObjectModelFramework\start_dockergrid.bat"
    subprocess.call(["START", "/B", script_name], shell=True)
    #sleep(30)
    if request.param == "chrome":
        chrome_options = Options()
        prefs = {
            "intl.accept_languages": "en-US"
        }
        chrome_options.add_experimental_option("prefs", prefs)
        if platform.system() == 'Linux' and platform.uname().processor == '':
          #  driver = webdriver.Remote(command_executor=remote_url, options=webdriver.ChromeOptions())
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        elif platform.system() == 'Windows' or platform.system() == 'Linux':
         #   driver = webdriver.Remote(command_executor=remote_url, options=webdriver.ChromeOptions())
           driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    if request.param == 'firefox':
        if platform.system() == 'Linux' and platform.uname().processor == '':
            driver = webdriver.Remote(command_executor=remote_url, options=webdriver.FirefoxOptions())
            #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif platform.system() == 'Windows' or platform.system() == 'Linux':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            #driver = webdriver.Remote(command_executor=remote_url, options=webdriver.FirefoxOptions())
    request.cls.driver = driver
    config = ConfigParser()
    config.read('ConfigurationData/configurationData.config')

    # url = config.get('basic-info', 'testSiteUrl')
    # driver.get(url)
    driver.get("https://explore-dev.vitalbook.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def setup_module(module):
    print('Creating DB Connection')
