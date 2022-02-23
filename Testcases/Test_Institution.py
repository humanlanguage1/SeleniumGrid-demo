from Pages.Page_Institutions import Institutions
from Pages.Page_LoginVitalSource import LoginVitalSource
from Testcases.BaseTest import BaseTest
from Utilities.configReader import readConfig

class Test_Institution(BaseTest):

    def test_searchInstitution(self):
        regPage = LoginVitalSource(self.driver)
        insPage = Institutions(self.driver)

        regPage.doLogin(readConfig("credentials", "username"), readConfig("credentials", "password"))
        insPage.close_modal()
        insPage.institution_search()

    def test_AddInstitution(self):
        regPage = LoginVitalSource(self.driver)
        insPage = Institutions(self.driver)

        regPage.doLogin(readConfig("credentials", "username"), readConfig("credentials", "password"))
        insPage.close_modal()
        insPage.institution_addInstitution()


