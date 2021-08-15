from behave import *
from selenium import webdriver
from features.pages.Login.LoginPage import LoginPage
from features.pages.Inventory.InventoryPage import InventoryPage
from features.config.config import Test_Data


@when(u'I login with valid username and password')
def step_impl(context):
    global loginPage
    loginPage = LoginPage(context.driver)
    loginPage.do_login(Test_Data.STANDARD_USER_NAME, Test_Data.PASSWORD)


@then(u'I should be on Inventory Page')
def step_impl(context):
    global inventoryPage
    inventoryPage = InventoryPage(context.driver)
    assert inventoryPage.get_title() == 'PRODUCTS'
    assert inventoryPage.check_url() == Test_Data.INVENTORY_URL


@when(u'I click add to cart button')
def step_impl(context):
    inventoryPage.add_to_cart()


@then(u'Cart icon should display 1')
def step_impl(context):
    assert inventoryPage.check_cart() == '1'


@then(u'Cart icon should display 2')
def step_impl(context):
    assert inventoryPage.check_cart() == '2'


@when(u'I click remove button')
def step_impl(context):
    inventoryPage.remove_from_cart()


@then(u'Cart icon should be empty')
def step_impl(context):
    inventoryPage.empty_cart()

@when(u'I click add to cart button for item "{item}"')
def step_impl(context, item):
    inventoryPage.add_item_to_cart(item)



@when(u'I click remove button for item "{item}"')
def step_impl(context, item):
    inventoryPage.remove_item_from_cart(item)


