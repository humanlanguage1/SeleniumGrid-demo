import pytest


@pytest.mark.usefixtures("log_on", "get_browser")
class BaseTest:
    pass
