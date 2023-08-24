from Cofigurations.locators import Locators
from Pages.BasePage import BasePage
from Utilities import CsvReader


class ReviewOrderPage(BasePage):

    def GetOrderDetails(self):
        ProductsDetails=[]
        end_of_page = False
        previous_page_source = self.driver.page_source
        while not end_of_page:
            Productnames = self.findelements(Locators.ReviewPageProductName)
            ProductPrices = self.findelements(Locators.ReviewPageProductPrice)
            if Productnames==None:#If there are no products come out of the loop
                break
            elif len(Productnames) > 1:
                for i in range(0, len(Productnames)):
                    product = [self.gettext(Productnames[i]), self.gettext(ProductPrices[i])]
                    #Add the product details into list if it is not present in that list
                    if product not in ProductsDetails:
                        ProductsDetails.append(product)
            else:
                ProductsDetails.append([self.gettext(Productnames[0]), self.gettext(ProductPrices[0])])
            self.scroll_to_bottom()
            end_of_page = previous_page_source == self.driver.page_source
        return ProductsDetails

    def GetOrderDetailsFromCSV(self):
        ProductDetails=CsvReader.read_csv_to_list()
        return ProductDetails


    def PlaceOrderIsVisible(self):
        return self.isdisplayed(Locators.PlaceOrder)

    def cliclonplaceorder(self):
        self.clickOn(Locators.PlaceOrder)

    def VerifyOrderDispatchMSG(self):
        return self.getElementText(Locators.OrderDispatched)

    def clickonContinueshopping(self):
        return self.clickOn(Locators.ContinueShopping)
