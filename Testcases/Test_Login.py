from Pages.Page_Institutions import Institutions
from Pages.Page_LoginVitalSource import LoginVitalSource
from Testcases.BaseTest import BaseTest
from Utilities.configReader import readConfig


class Test_Login(BaseTest):

    def test_Login_Successful(self):
        regPage = LoginVitalSource(self.driver)
        regPage.doLogin(readConfig("credentials", "username"), readConfig("credentials", "password"))

        instPage = Institutions(self.driver)
        instPage.close_modal()

        assert instPage.getTextH1() == 'Institutions'

