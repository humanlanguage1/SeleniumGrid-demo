from Pages.Page_Institutions import Institutions
from Pages.Page_LoginVitalSource import LoginVitalSource
from Pages.Page_Market import Market
from Testcases.BaseTest import BaseTest
from Utilities.configReader import readConfig

class Test_Market(BaseTest):

    def test_createOffer(self):
        regPage = LoginVitalSource(self.driver)
        insPage = Institutions(self.driver)
        marketPage = Market(self.driver)

        regPage.doLogin(readConfig("credentials", "username"), readConfig("credentials", "password"))
        insPage.close_modal()
        marketPage.goToMarketplace()
        marketPage.searchCollection()
        marketPage.clickSelectedCollection()
        marketPage.createOffer()
        marketPage.selectOfferType()
        marketPage.typeInstitutionSelection()

    def test_checkOfferStatus(self):
        regPage = LoginVitalSource(self.driver)
        insPage = Institutions(self.driver)
        marketPage = Market(self.driver)

        regPage.doLogin(readConfig("credentials", "username"), readConfig("credentials", "password"))
        insPage.close_modal()
        marketPage.goToMarketplace()
        marketPage.searchCollection()
        marketPage.clickSelectedCollection()
        assert marketPage.checkOffer() == '31 Active Subscriptions'

