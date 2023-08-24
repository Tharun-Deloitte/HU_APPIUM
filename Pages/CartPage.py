from Cofigurations.locators import Locators
from Pages.BasePage import BasePage
from Utilities import CsvReader


class CartPage(BasePage):

    def getcartcount(self):
        return int(self.getElementText(Locators.cartcount))

    # def deleteoneItem(self):
    #     product=CsvReader.get_last_line_as_list()
    #     #deletes the last added product
    #     end_of_page = False
    #     previous_page_source = self.driver.page_source
    #     while not end_of_page:
    #         Elements = self.findelements(Locators.cartpageProductNames)
    #         RemoveItemElements = self.findelements(Locators.removeitem)
    #         if (len(Elements) > 1):
    #             for i in range(0, len(Elements)):
    #                 productname = Elements[i].text
    #                 print(productname)
    #                 if (productname == product[0]):
    #                     RemoveItemElements[i].click()
    #                     CsvReader.delete_row_by_value(productname)
    #                     break
    #         else:
    #             self.clickOn(Locators.removeitem)
    #         print("doing scroll")
    #         self.scroll_to_bottom()
    #         end_of_page = previous_page_source == self.driver.page_source
    #         previous_page_source = self.driver.page_source

    def deleteoneItem(self):
        product=CsvReader.get_first_line_as_list()
        #deletes the first added product
        Elements = self.findelements(Locators.cartpageProductNames)
        if (len(Elements) > 1):
            for i in range(0, len(Elements)):
                productname = Elements[i].text
                print(productname)
                if (productname == product[0]):
                    RemoveItemElements = self.findelements(Locators.removeitem)
                    ProductquantityElements=self.findelements(Locators.cartpageProductQuantity)
                    RemoveItemElements[i].click()
                    CsvReader.delete_row_by_value(productname)
                    return int(ProductquantityElements[i].text)
        else:
            self.clickOn(Locators.removeitem)
            return int(self.getElementText(Locators.cartpageProductQuantity))




    def clickonCheckout(self):
        self.clickOn(Locators.ProceedtoCheckOut)