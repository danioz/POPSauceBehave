import time

from behave import *
from selenium import webdriver
from features.pages.Login.LoginPage import LoginPage
from features.pages.Inventory.InventoryPage import InventoryPage
from features.config.config import Test_Data


@given(u'I am on SauceDemo LoginPage')
def step_impl(context):
    global loginPage
    loginPage = LoginPage(context.driver)
    assert loginPage.get_title() == Test_Data.TITLE
    assert loginPage.check_url() == Test_Data.BASE_URL


@when(u'I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    loginPage.input_username(username)
    loginPage.input_password(password)


@when(u'I click on login button')
def step_impl(context):
    loginPage.click_login()


@then(u'I should be successfully login to the Inventory page')
def step_impl(context):
    inventoryPage = InventoryPage(context.driver)
    assert inventoryPage.get_title() == 'PRODUCTS'
    assert inventoryPage.check_url() == Test_Data.INVENTORY_URL


@then(u'System should display "{message}"')
def step_impl(context, message):
    assert loginPage.get_error_message() == message
