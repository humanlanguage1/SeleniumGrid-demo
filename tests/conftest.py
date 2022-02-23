import json
import pytest
from pages.base_page import BasePage
from pages.home_page import HomePage

CONFIG_PATH = "F:\\Code\\Python\\SeleniumPy\\tests\\config.json"
SUPPORTED_BROWSERS = ['CHROME', 'FIREFOX']

# https://blog.testproject.io/2019/07/16/read-config-files-in-python-selenium
@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        config = json.load(config_file)
    # Validate and return the browser choice from the config data
    if BasePage.KV_BROWSER not in config:
        raise Exception(f'The config file does not contain "{BasePage.KV_BROWSER}"')
    elif config[BasePage.KV_BROWSER] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config[BasePage.KV_BROWSER]}" is not a supported browser')
    # Validate and return other needed data
    if BasePage.KV_PLATFORM not in config:
        raise Exception(f'The config file does not contain "{BasePage.KV_PLATFORM}"')
    if BasePage.KV_HUB_URL not in config:
        raise Exception(f'The config file does not contain "{BasePage.KV_HUB_URL}"')
    if BasePage.KV_BASE_URL not in config:
        raise Exception(f'The config file does not contain "{BasePage.KV_BASE_URL}"')
    return config

#https://www.py4u.net/discuss/146481: "# Teardown : logic is guaranteed to run regardless of what happens during the tests."
#However, saw that if run the node without a timeout, the chrome instance is not made available
@pytest.fixture
def home_page(request, config):
    page = HomePage(config)
    request.cls.page = page
    yield
    page.close()