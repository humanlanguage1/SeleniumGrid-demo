from Pages.BasePage import BasePage


class Institutions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def close_modal(self):
        self.click("modal_x_XPATH")

    def getTextH1(self):
        return self.getText("label_h1_XPATH")

    def institution_search(self):
        self.send_value("institucionesPage_searchBar_XPATH", 'peru')
        self.sendText()

    def institution_addInstitution(self):
        self.click("institucionesPage_addInstitution_XPATH")

