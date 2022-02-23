from Pages.Page_Collections import Collections
from Pages.Page_Institutions import Institutions
from Pages.Page_LoginVitalSource import LoginVitalSource
from Testcases.BaseTest import BaseTest
from Utilities.configReader import readConfig

class Test_Colecciones(BaseTest):

    def test_AddCollection(self):
        regPage = LoginVitalSource(self.driver)
        insPage = Institutions(self.driver)
        collPage = Collections(self.driver)

        regPage.doLogin(readConfig("credentials", "username"), readConfig("credentials", "password"))
        insPage.close_modal()
        collPage.goToCollectionsPage()
        collPage.clickCreateCollections()
        collPage.typeCollectionName()
        collPage.clickProviderDropdown()
        collPage.typeProviderName()
        collPage.createCollection()

