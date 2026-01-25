from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login import LoginPage
from tests.pages.inventory import InventoryPage
import pytest

scenarios('../features/inventory.feature')

@given('I am on the SauceDemo login page')
def go_to_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")

@when(parsers.parse('I login with username "{username}" and password "{password}"'))
def login(page, username, password):
    login_page = LoginPage(page)
    login_page.login(username, password)

@then('I should be redirected to the inventory page')
def check_inventory_page(page):
    inventory_page = InventoryPage(page)
    assert inventory_page.is_at()

@given(parsers.parse('I am logged in as "{username}" with password "{password}"'))
def logged_in(page, username, password):
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    assert inventory_page.is_at()

@when(parsers.parse('I add the item "{item_name}" to the cart'))
def add_item(page, item_name):
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart(item_name)

@then(parsers.parse('the cart badge should show "{count}"'))
def cart_badge_count(page, count):
    inventory_page = InventoryPage(page)
    assert inventory_page.get_cart_count() == int(count)

@given(parsers.parse('I have "{item_name}" in my cart'))
def have_item_in_cart(page, item_name):
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login('standard_user', 'secret_sauce')
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart(item_name)
    assert inventory_page.get_cart_count() == 1

@when(parsers.parse('I remove the item "{item_name}" from the cart'))
def remove_item(page, item_name):
    inventory_page = InventoryPage(page)
    inventory_page.remove_from_cart(item_name)

@then('the cart badge should not be visible')
def cart_badge_not_visible(page):
    inventory_page = InventoryPage(page)
    assert not inventory_page.is_cart_badge_visible()
