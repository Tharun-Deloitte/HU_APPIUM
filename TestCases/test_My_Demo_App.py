import logging

import allure
import pytest

from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckOutPage
from Pages.HomeScreen import HomeScreen
from Pages.LoginPage import LoginPage
from Pages.PaymentPage import PaymentPage
from Pages.ReviewOrderPage import ReviewOrderPage
from Utilities.LogUtil import Logger
from Utilities.constants import constants

log = Logger(__name__, logging.INFO)


@pytest.mark.usefixtures("log_on_failure", "appium_driver", "setup_function")
class Test_MyDemoApp:

    def setup_method(self):
        self.home = HomeScreen(self.driver)
        self.login = LoginPage(self.driver)
        self.cart = CartPage(self.driver)
        self.checkout = CheckOutPage(self.driver)
        self.payment = PaymentPage(self.driver)
        self.review = ReviewOrderPage(self.driver)

    @pytest.mark.smoke
    @allure.description("Profile login with Invalid username and password")
    @allure.severity("critical")
    def test_InvalidLogin(self):
        self.home.clickmenu()
        self.home.clickLoginHomePage()
        self.login.EnterUserName(constants.InvalidUsername)
        self.login.EnterPassword(constants.InvalidPassword)
        self.login.clickonLogin()
        ErroeMSG=self.login.ErrorMsgVerify()
        try:
            assert ErroeMSG == constants.InvalidLoginErrorMSG
            log.logger.info("Invalid login error msg is displayed properly")
        except AssertionError:
            log.logger.info("Invalid login error msg is not displayed properly")
            assert False

    @pytest.mark.smoke
    @allure.description("Profile login with Valid username and password")
    @allure.severity("critical")
    def test_ValidLogin(self):
        self.home.clickmenu()
        self.home.clickLoginHomePage()
        self.login.EnterUserName(constants.ValidUsename)
        self.login.EnterPassword(constants.ValidPassword)
        self.login.clickonLogin()
        log.logger.info("Successfully Logged IN")
        boolean = self.home.verifylogin()

        try:
            assert boolean
            log.logger.info("Login verified")
        except AssertionError:
            log.logger.info("Login Failed")
            assert False

    @pytest.mark.regression
    @allure.description("Verifying whether the products are sorted according to their name")
    @allure.severity("Normal")
    def test_NameSorting(self):
        ProductsBeforeSorting = self.home.GetProductNames()
        self.home.clickonsortbutton()
        self.home.clickonNameAscending()
        ProductsAfterSorting = self.home.GetProductNames()
        ProductsBeforeSorting.sort()
        try:
            assert ProductsAfterSorting == ProductsBeforeSorting
            log.logger.info("Product sorting is done properly")
        except AssertionError:
            log.logger.info("Product sorting is not done properly")
            assert False


    @pytest.mark.regression
    @allure.description("Verifying whether the products are sorted according to their Price")
    @allure.severity("Normal")
    def test_PriceSorting(self):
        PriceListBeforeSorting = self.home.GetPriceNames()
        self.home.clickonsortbutton()
        self.home.clickonPriceDescending()
        PricelistAfterSorting = self.home.GetPriceNames()
        PriceListBeforeSorting.sort(reverse=True)  # reverse is true because sorted descending
        try:
            assert PricelistAfterSorting == PriceListBeforeSorting
            log.logger.info("Price sorting is done properly")
        except AssertionError:
            log.logger.info("Price sorting is not done properly")
            assert False


    @pytest.mark.smoke
    @allure.description("Verifying weather the user cart number is updated after deleting the item")
    @allure.severity("Critical")
    def test_AddandDeleteproducts(self):
        self.home.addmultipleproducts(5)
        self.home.clickoncart()
        CartCountBefore = self.home.getcartcount()
        DeleteItemQuantity=self.cart.deleteoneItem()
        CartCountAfter = self.home.getcartcount()
        try:
            assert CartCountBefore == (CartCountAfter + DeleteItemQuantity)
            log.logger.info("Cart count is updated properly")
        except AssertionError:
            log.logger.info("Cart count is not updated properly")
            assert False

    @pytest.mark.functional
    @allure.description("Verifying If the Payment page error messages are displayed if user dont enter anything and click on go to review order page")
    @allure.severity("Critical")
    def test_VerifyPaymentPageErrorMsgWithOutEnteringDetails(self):
        self.cart.clickonCheckout()
        self.checkout.filldetails()
        self.checkout.clickonGoToPayment()
        self.payment.clickonReviewOrder()
        Cardmsg = self.payment.CardNumErrorMSG()
        cvvmsg = self.payment.cvverrormsg()
        Expirymsg = self.payment.Expiryerrormsg()
        try:
            assert Cardmsg == constants.Paymenterrormsg
            assert cvvmsg == constants.Paymenterrormsg
            assert Expirymsg == constants.Paymenterrormsg
            log.logger.info("Payment page error msg are displayed properly")
        except AssertionError:
            log.logger.info("Payment page error msg are not displayed properly")
            assert False


    @pytest.mark.functional
    @allure.description("Verifying If the Payment page error messages are displayed if user enters Invalid details")
    @allure.severity("Critical")
    def test_VerifyPaymentPageErrorMsgInvalidDetails(self):
        self.payment.fillInvaliddetails()
        self.payment.clickonReviewOrder()
        Cardmsg = self.payment.CardNumErrorMSG()
        # cvvmsg=self.payment.cvverrormsg()
        # Expirymsg=self.payment.Expiryerrormsg()
        try:
            assert Cardmsg == constants.Paymenterrormsg
            # assert cvvmsg==constants.Paymenterrormsg
            # assert Expirymsg==constants.Paymenterrormsg
            log.logger.info("Payment page error msg are displayed properly")
        except AssertionError:
            log.logger.info("Payment page error msg are not displayed properly")
            assert False


    @pytest.mark.functional
    @allure.description("Verifying If the user can goto Review Order page by entering wrong payment details")
    @allure.severity("Critical")
    def test_GoingtoReviewOrderInvalidPaymentDetails(self):
        self.payment.clickonReviewOrder()
        boolean=self.review.PlaceOrderIsVisible()
        try:
            assert boolean==False
            log.logger.info("User is not able to go to Review order page by entering wrong payment details")
        except AssertionError:
            log.logger.info("User is able to go to Review order page by entering wrong payment details")




    @pytest.mark.functional
    @allure.description("Verifying Products displayed in Review order page")
    @allure.severity("Critical")
    def test_verifyReviewPageProductDetails(self):
        self.payment.GoTOPreviousPage()
        self.payment.fillValiddetails()
        self.payment.clickonReviewOrder()

        ProductDetailsFromReviewOrderPage = self.review.GetOrderDetails()
        ProductDetailsFromCSV = self.review.GetOrderDetailsFromCSV()
        print(ProductDetailsFromCSV)
        print(ProductDetailsFromReviewOrderPage)
        try:
            assert ProductDetailsFromReviewOrderPage == ProductDetailsFromCSV
            log.logger.info("Product details are matching in Review order page")
        except AssertionError:
            log.logger.info("Product details are not matching in Review order page")
            log.logger.info(ProductDetailsFromReviewOrderPage)
            log.logger.info(ProductDetailsFromCSV)
            assert False


    @pytest.mark.functional
    @allure.description("Verifying order success msg by placing the order")
    @allure.severity("Critical")
    def test_verifyordersuccessmsg(self):
        self.review.cliclonplaceorder()
        orderdispatchmsg = self.review.VerifyOrderDispatchMSG()
        try:
            assert orderdispatchmsg == constants.OrderDispatchedMSG
            log.logger.info("Order dispatch message is displayed properly")
        except AssertionError:
            log.logger.info("Order dispatch message is not displayed properly")
            log.logger.info(orderdispatchmsg)
        self.review.clickonContinueshopping()


    @pytest.mark.functional
    @allure.description("Verifying if the user is able to log out")
    @allure.severity("Critical")
    def test_logout(self):
        self.home.Wait()
        self.home.scroll_to_top()
        self.home.clickmenu()
        self.home.ClickonLogout()
        self.home.ClickonLogoutConfirmation()
        Msg = self.home.GetLogoutSuccessMSG()
        self.home.ClickonSuccessOk()
        try:
            assert Msg == constants.LogOutSuccess
            log.logger.info("Log out success msg is displayed as expected")
        except AssertionError:
            log.logger.info("Log out success msg is not displayed as expected")
            log.logger.info(Msg)
            assert False


    @pytest.mark.functional
    @allure.description("Verifying if all menu options are displayed")
    @allure.severity("Critical")
    def test_VerifyMenuButtons(self):
        self.home.clickmenu()
        boolean=self.home.VerifyAllMenuButtons()
        try:
            assert boolean
            log.logger.info("All menu options are present")
        except AssertionError:
            log.logger.info("All menu options are not displayed")
            assert False





