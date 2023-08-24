from Cofigurations.locators import Locators
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def EnterUserName(self,username):
        self.Sendkeys(Locators.UsernameInput,username)

    def EnterPassword(self,password):
        self.Sendkeys(Locators.PasswordInput,password)

    def clickonLogin(self):
        self.clickOn(Locators.LoginpageLoginBtn)

    def ErrorMsgVerify(self):
        Errormsg=self.getElementText(Locators.detailsNotMatch)
        return Errormsg






