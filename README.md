# POPSauceBehave

This is an example of a python framework with the page object pattern.

# Requirements
- selenium 
- behave
- allure-behave  
- webdriver-manager

# Status
Implemented :
- LoginPage.feature
- InventoryPage.feature
- ItemPage.feature

# Generate Test Report
To generate all tests report using Allure you need to run tests by command first:

```
behave -f allure_behave.formatter:AllureFormatter -o reports/ features
```
Then you need to use command:
```
allure serve reports/
```