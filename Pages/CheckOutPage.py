from Cofigurations.locators import Locators
from Pages.BasePage import BasePage
from Utilities.constants import constants

class CheckOutPage(BasePage):


    def filldetails(self):
        self.Sendkeys(Locators.FullName,constants.FullName)
        self.Sendkeys(Locators.Address1,constants.Address1)
        self.Sendkeys(Locators.City,constants.city)
        self.Sendkeys(Locators.State,constants.state)
        self.Sendkeys(Locators.PinCode,constants.pincode)
        self.Sendkeys(Locators.Country,constants.country)
    def clickonGoToPayment(self):
        self.clickOn(Locators.ToPayment)
