from Pages.BasePage import BasePage


class LoginVitalSource(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def doLogin(self, username, password):
        self.send_value("username_XPATH", username)
        self.send_value("password_XPATH", password)
        self.click("submit_XPATH")