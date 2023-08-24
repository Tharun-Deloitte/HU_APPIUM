import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from Utilities import CsvReader


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="class")
def appium_driver(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = 'ARapp'
    desired_caps['app'] = 'C://Users//naratreddy//Desktop//MainAssignment//HU_APPIUM//App//Android-MyDemoAppRN.1.3.0.build-244.apk'
    desired_caps['automationName'] = 'UiAutomator2'
    # desired_caps['noReset'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723', desired_caps)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    driver = appium_driver
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(scope='class')
def setup_function():
    CsvReader.delete_csv_data()