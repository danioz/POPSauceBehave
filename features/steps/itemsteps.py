import time

from behave import *
from selenium import webdriver
from features.pages.Login.LoginPage import LoginPage
from features.pages.Inventory.InventoryPage import InventoryPage
from features.pages.Item.ItemPage import ItemPage
from features.config.config import Test_Data


@when(u'I click at "{item}" title at Inventory page')
def step_impl(context, item):
    global inventoryPage
    inventoryPage = InventoryPage(context.driver)
    inventoryPage.add_item_link(item)


@then(u'I should be at Item page')
def step_impl(context):
    global itemPage
    itemPage = ItemPage(context.driver)
    assert Test_Data.ITEM_URL in itemPage.check_url()

@when(u'I click add to cart button at item page')
def step_impl(context):
    itemPage.add_to_cart()

@when(u'I click remove button at item page')
def step_impl(context):
    itemPage.remove_from_cart()


@when(u'I check name of the "{item}" at Inventory page')
def step_impl(context, item):
    global inventoryPage
    inventoryPage = InventoryPage(context.driver)
    global name
    name = inventoryPage.get_item_name(item)
    return name


@when(u'I check description of the "{item}" at Inventory page')
def step_impl(context, item):
    global description
    description = inventoryPage.get_item_description(item)
    return description


@when(u'I check price of "{item}" at Inventory page')
def step_impl(context, item):
    global price
    price = inventoryPage.get_item_price(item)
    return price


@then(u'Name of "{item}" should match at Item page')
def step_impl(context, item):
    assert itemPage.get_item_name() == name


@then(u'Description of "{item}" should match at Item page')
def step_impl(context, item):
    assert itemPage.get_item_description() == description


@then(u'Price of "{item}" should match at Item page')
def step_impl(context, item):
    assert itemPage.get_item_price() == price
