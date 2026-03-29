from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login import LoginPage
from tests.pages.inventory import InventoryPage
from tests.pages.cart import CartPage
import pytest

scenarios('../checkout.feature')


@when('I view the cart')
def view_cart(page):
    # Click the cart icon to navigate to the cart page
    page.locator('.shopping_cart_link').click()
    cart_page = CartPage(page)
    # Wait for the cart page to load
    page.wait_for_url("**/cart.html")
    assert cart_page.is_at_cart_page()

@then('button "Continue Shopping" should be visible')
def continue_shopping_button_visible(page):
    cart_page = CartPage(page)
    assert cart_page.is_continue_shopping_visible()


@when(parsers.parse('I remove the item "{item_name}" from the cart'))
def remove_item_from_cart(page, item_name):
    cart_page = CartPage(page)
    cart_page.remove_item(item_name)

@then('the cart should be empty')
def cart_should_be_empty(page):
    cart_page = CartPage(page)
    page.wait_for_timeout(500)  # Wait for the cart to update after removal
    assert cart_page.is_empty()

@then('the cart should not be empty')
def cart_should_not_be_empty(page):
    cart_page = CartPage(page)
    assert not cart_page.is_empty(), "Cart should contain items but is empty"

@when(parsers.parse('I click the "{button_text}" button'))
def click_cart_button(page, button_text):
    cart_page = CartPage(page)
    cart_page.click_button(button_text)

@then('I should be redirected to the inventory page')
def redirected_to_inventory(page):
    inventory_page = InventoryPage(page)
    assert inventory_page.is_at()

@then('the checkout page should be displayed')
def checkout_page_displayed(page):
    cart_page = CartPage(page)
    assert cart_page.is_at_checkout()

@when(parsers.parse('I fill in the checkout information with first name "{first_name}", last name "{last_name}", and postal code "{postal_code}"'))
def fill_checkout_info(page, first_name, last_name, postal_code):
    cart_page = CartPage(page)
    cart_page.fill_checkout_info(first_name, last_name, postal_code)

@when('I continue to the overview page')
def continue_to_overview(page):
    cart_page = CartPage(page)
    cart_page.continue_to_overview()

@then(parsers.parse('I should see "{item_name}" in the checkout summary'))
def should_see_item_in_summary(page, item_name):
    cart_page = CartPage(page)
    assert cart_page.is_item_in_summary(item_name)

@when('I finish the checkout')
def finish_checkout(page):
    cart_page = CartPage(page)
    cart_page.finish_checkout()

@then(parsers.parse('I should see the message "{message}"'))
def should_see_checkout_complete_message(page, message):
    cart_page = CartPage(page)
    assert cart_page.is_checkout_complete_displayed(message)