from Pages.BasePage import BasePage

class Collections(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def goToCollectionsPage(self):
        self.click("navigationBar_collectionsButton_xpath")

    def clickCreateCollections(self):
        self.click("collectionsPage_addCollection_xpath")

    def typeCollectionName(self):
        self.send_value("collectionsPage_addCollection_input_xpath", 'English')

    def clickProviderDropdown(self):
        self.click("collectionsPage_selectProvider_dropdown_xpath")

    def typeProviderName(self):
        self.send_value("collectionsPage_selectProvider_searchBar_xpath", 'crisol')

    def createCollection(self):
        #Confirming the dropdown button
        self.click("collectionsPage_selectProvider_Result_xpath")
        #creating collection by clicking the button "Create Collection"
        self.click("collectionsPage_createCollectionButton_xpath")


