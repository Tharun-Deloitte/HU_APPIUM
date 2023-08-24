import logging

from Cofigurations.locators import Locators
from Pages.BasePage import BasePage
from Utilities import CsvReader
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verifylogin(self):
        boolean=self.isdisplayed(Locators.srot)
        return boolean


    def clickmenu(self):
        self.clickOn(Locators.menuBtn_locator)

    def Wait(self):
        self.driver.implicitly_wait(5)

    def clickLoginHomePage(self):
        self.clickOn(Locators.options_LogIN)

    def clickonsortbutton(self):
        self.clickOn(Locators.srot)

    def clickonPriceDescending(self):
        self.clickOn(Locators.PriceDescen)

    def GetList(self,locator):
        ProductNames=[]
        TotalElements=[]
        end_of_page = False
        previous_page_source = self.driver.page_source
        while not end_of_page:
            Elements = self.findelements(locator)
            for i in range(0, len(Elements)):
                if Elements[i] not in TotalElements:
                    TotalElements.append(Elements[i])
                    ProductNames.append(self.gettext(Elements[i]))
            self.scroll_to_bottom()
            end_of_page = previous_page_source == self.driver.page_source
            previous_page_source = self.driver.page_source
        self.scroll_to_top()
        return ProductNames


    def GetProductNames(self):
        ProductNames=self.GetList(Locators.productNames)
        return ProductNames

    def GetPriceNames(self):
        PriceList=self.GetList(Locators.ProductPrices)
        for i in range(0,len(PriceList)):
            PriceList[i]=float(PriceList[i].replace("$",''))
        return PriceList


    def addmultipleproducts(self,NoOfProductsToAdd):
        TotalProducts = []
        end_of_page = False
        ProductsAddedcount=0
        previous_page_source = self.driver.page_source
        while not end_of_page and ProductsAddedcount<NoOfProductsToAdd:
            ProductElements = self.findelements(Locators.productNames)
            if len(ProductElements) > 1:
                for i in range(0, len(ProductElements)):
                    if ProductElements[i] not in TotalProducts and ProductsAddedcount<NoOfProductsToAdd:
                        ProductElements[i].click()
                        TotalProducts.append(ProductElements[i])
                        self.clickOn(Locators.Addtocart)
                        ProductsAddedcount=ProductsAddedcount+1
                        print(ProductsAddedcount)
                        self.storeproductdetails()
                        self.driver.back()
                        break
            else:
                if(ProductsAddedcount<NoOfProductsToAdd):
                    if ProductElements[i] not in TotalProducts:
                        ProductElements[i].click()
                        TotalProducts.append(ProductElements[i])
                        self.clickOn(Locators.Addtocart)
                        ProductsAddedcount = ProductsAddedcount + 1
                        print(ProductsAddedcount)
                        self.storeproductdetails()
                        self.driver.back()
            self.scroll_to_bottom()
            end_of_page = previous_page_source == self.driver.page_source
            previous_page_source = self.driver.page_source



    def storeproductdetails(self):
        ProductName=self.getElementText(Locators.ProductName)
        ProductPrice=self.getElementText(Locators.ProductPrice)
        # ProductQuantity=self.getElementText("Product Quantity",Locators.ProductQuantity)
        log.logger.info(ProductName+" is added to the cart")
        Product=[ProductName,ProductPrice]
        print(Product)
        CsvReader.write_to_csv(Product)


    def clickoncart(self):
        self.clickOn(Locators.GoToCart)

    def getcartcount(self):
        count=int(self.getElementText(Locators.cartcount))
        if count is not None:
            return count
        else:
            return 0


    def clickonNameAscending(self):
        self.clickOn(Locators.NameAscen)

    def ClickonLogout(self):
        self.clickOn(Locators.options_LogOut)

    def ClickonLogoutConfirmation(self):
        self.clickOn(Locators.popuplogout)

    def GetLogoutSuccessMSG(self):
        return self.getElementText(Locators.succseefullogoutmsg)

    def ClickonSuccessOk(self):
        self.clickOn(Locators.SuccessOk)

    def VerifyAllMenuButtons(self):
        # performing boolean and operation for each response so that if
        # even one of the response is false then final output will be false
        boolean=self.isdisplayed(Locators.options_Catlog)
        boolean = boolean & self.isdisplayed(Locators.options_WebView)
        boolean = boolean & self.isdisplayed(Locators.options_QRCode)
        boolean = boolean & self.isdisplayed(Locators.options_GeoLocation)
        boolean = boolean & self.isdisplayed(Locators.options_Draw)
        boolean = boolean & self.isdisplayed(Locators.options_About)
        boolean = boolean & self.isdisplayed(Locators.options_Reset)
        boolean = boolean & self.isdisplayed(Locators.options_FingerPrint)
        boolean = boolean & self.isdisplayed(Locators.options_LogIN)
        boolean = boolean & self.isdisplayed(Locators.options_LogOut)
        boolean = boolean & self.isdisplayed(Locators.options_APICalls)
        boolean = boolean & self.isdisplayed(Locators.options_BotVideo)
        return boolean



