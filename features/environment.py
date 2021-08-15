from behave import *

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.config.config import Test_Data


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.headless = True
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    context.driver.delete_all_cookies()
    context.driver.get(Test_Data.BASE_URL)


def after_scenario(context, scenario):
    context.driver.close()
