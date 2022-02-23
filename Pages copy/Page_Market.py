from Pages.BasePage import BasePage


class Market(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def goToMarketplace(self):
        self.click("navigationBar_MarketButton_XPATH")

    def searchCollection(self):
        self.send_value("marketPage_searchBarInput_XPATH", 'English')

    def clickSelectedCollection(self):
        self.click("marketPage_SelectedCollection_XPATH")

    def createOffer(self):
        self.click("marketPage_createOfferButton_XPATH")
        self.click("marketPage_OfferNextButton_XPATH")

    def selectOfferType(self):
        self.click("marketPage_selectOfferType_XPATH")

    def typeInstitutionSelection(self):
        self.send_value("marketPage_Institution_Selection_Input_XPATH", 'peru')

    def checkOffer(self):
        self.getText("marketPage_SelectedCollection_XPATH")

