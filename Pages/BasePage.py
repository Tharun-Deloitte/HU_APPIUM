import logging

from appium.webdriver.common.touch_action import TouchAction
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def clickOn(self,locator):
        try:
            # Perform actions on the element
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator[1]))
            element.click()

        except StaleElementReferenceException:
            # Handle the stale element reference exception by re-locating the element
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator[1]))
            element.click()
        except Exception as e:
            log.logger.info("Cannot find element "+locator[0])
            log.logger.info("An error occured "+str(e))
            return
        log.logger.info("Clicking on "+locator[0]+" button")

    def isdisplayed(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator[1]))
            log.logger.info(locator[0] + " is displayed")
            return bool(element)
        except Exception as e:
            log.logger.info("The element "+locator[0]+" is not displayed")
            log.logger.info("An error occured "+str(e))
            return False


    def Sendkeys(self,locator,keyvalue):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator[1])).clear().send_keys(keyvalue)
        except StaleElementReferenceException:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator[1])).clear().send_keys(keyvalue)
        except Exception as e:
            log.logger.info("Cannot enter text at "+locator[0])
            log.logger.info("An error occured"+str(e))
            return
        log.logger.info("Entered text in "+locator[0]+" field")

    def getElementText(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator[1]))
            log.logger.info("The text at "+ locator[0] + " is "+element.text)
            return element.text.strip()
        except:
            log.logger.info(("There is no text at the given locator "+locator[0]))
            return None




    def findelements(self,locator):
        try:
            elements=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(locator[1]))
            log.logger.info("Found "+str(len(elements))+" elements at "+ locator[0])
            return elements
        except Exception as e:
            log.logger.info("Cannot find the element "+locator[0])
            log.logger.info("An error occured " + str(e))
            return None


    def gettext(self,locator_element):
        return locator_element.text

    def scroll_to_top(self):
        window_size = self.driver.get_window_size()
        width = window_size['width']
        start_y = int(window_size['height'] * 0.2)
        end_y = int(window_size['height'] * 0.8)
        duration = 200
        action = TouchAction(self.driver)
        action.press(x=width // 2, y=start_y).wait(duration).move_to(x=width // 2, y=end_y).release().perform()

    def scroll_to_bottom(self):
        window_size = self.driver.get_window_size()
        width = window_size['width']
        start_y = int(window_size['height'] * 0.7)
        end_y = int(window_size['height'] * 0.5)
        duration = 200
        action = TouchAction(self.driver)
        action.press(x=width // 2, y=start_y).wait(duration).move_to(x=width // 2, y=end_y).release().perform()





