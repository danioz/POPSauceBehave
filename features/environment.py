from behave import *

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.config.config import Test_Data


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get(Test_Data.BASE_URL)


def after_scenario(context, scenario):
    context.driver.close()
