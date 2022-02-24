import os
import platform
import subprocess
from time import sleep

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture()
def log_on_failure(request, chrome_browser):
    yield
    item = request.node
    driver = chrome_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)
    if platform.system() == 'Linux':
      #  os.system('cd ' + BASE_DIR)
       # os.system('docker-compose down &')
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def chrome_browser():
    global driver
    remote_url = "http://localhost:4444/wd/hub"
    script_ini_w = "start_dockergrid.bat"
    # script_name = BASE_DIR + script_ini_w
    # script_name = r"C:\Users\USER\PycharmProjects\PageObjectModelFramework\start_dockergrid.bat"
  #  if platform.system() == 'Windows':
       #subprocess.call(["cd", BASE_DIR], shell=True)
    #    subprocess.call(["START", "/B", script_ini_w], shell=True)
        # subprocess.call(["START", "/B", "docker-compose", "up"], shell=True)
   # else:
   #     os.system('cd ' + BASE_DIR)
     #   os.system('docker-compose up &')
        # subprocess.call(["cd", BASE_DIR], shell=True)
        # subprocess.call(["chmod", "+x", script_ini_l], shell=True)
        # subprocess.call(["sh", script_ini_l], shell=True)
    #sleep(20)
  #  driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver = webdriver.Remote(command_executor=remote_url, options=webdriver.ChromeOptions())
    driver.get("https://facebook.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
