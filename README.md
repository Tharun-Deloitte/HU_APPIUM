# HU_APPIUM

In this I have used Python with Appium to test the  Swag Labs mobile application followed PageObject model and Pytest framework 

Configured the desired capabilities in Conftest.py file 
Used CSV file implementation to store Product details that are added to cart and used them to verify product details in Order summary page.

Logging and Allure reports is also implemented 
Log files and Screenshots of failed test cases are attached to the allure report

Command to run tests is:
pytest LocationOfTestFile -v -s --alluredir=LocationOfAllureReportFolder

Command to open allure report:
allure serve location of aLocationOfAllureReportFolder
