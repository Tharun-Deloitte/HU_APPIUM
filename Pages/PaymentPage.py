from Cofigurations.locators import Locators
from Pages.BasePage import BasePage
from Utilities.constants import constants


class PaymentPage(BasePage):

    def clickonReviewOrder(self):
        self.clickOn(Locators.ReviewOrder)


    def filldetails(self,name,cardnum,cvv,expiry):
        self.Sendkeys(Locators.FullName,name)
        self.Sendkeys(Locators.Cardnumber,cardnum)
        self.Sendkeys(Locators.Cvv,cvv)
        self.Sendkeys(Locators.Expirydate,expiry)

    def fillInvaliddetails(self):
        self.filldetails(constants.FullName,constants.Invalidcard,constants.Invaldcvv,constants.InvalidExpir)

    def fillValiddetails(self):
        self.filldetails(constants.FullName,constants.cardnumber,constants.cvv,constants.Expiry)
    def cvverrormsg(self):
        return self.getElementText(Locators.CvvErrorMsg)

    def Expiryerrormsg(self):
        return self.getElementText(Locators.ExpirationdateErrorMsg)

    def CardNumErrorMSG(self):
        return self.getElementText(Locators.CardnumErrorMsg)

    def GoTOPreviousPage(self):
        self.driver.back()
