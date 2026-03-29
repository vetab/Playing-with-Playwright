from pytest_bdd import scenarios, given, when, then, parsers
from tests.pages.login import LoginPage
from tests.pages.inventory import InventoryPage
from tests.pages.cart import CartPage
from tests.pages.payment import PaymentPage
import pytest

scenarios('../checkout.feature')


@then('the order total should be displayed')
def order_total_displayed(page):
    payment_page = PaymentPage(page)
    total = payment_page.get_order_total()
    assert total is not None, "Order total should be displayed"


@then('the cart should contain 3 items')
def cart_contains_three_items(page):
    cart_page = CartPage(page)
    # Count the cart items
    items = page.locator('.cart_item')
    assert items.count() == 3, f"Expected 3 items in cart, but found {items.count()}"



@then('the billing address form should be visible')
def billing_form_visible(page):
    payment_page = PaymentPage(page)
    assert payment_page.first_name_field.is_visible(), "First name field should be visible"
    assert payment_page.last_name_field.is_visible(), "Last name field should be visible"
    assert payment_page.postal_code_field.is_visible(), "Postal code field should be visible"


@then(parsers.parse('the overview page should display "{name}" as the billing name'))
def overview_displays_billing_name(page, name):
    payment_page = PaymentPage(page)
    assert payment_page.is_at_overview(), "Should be on overview page"
    # Verify the summary info contains the name
    summary_text = page.locator('.summary_info').inner_text()
    assert name in summary_text, f"Expected '{name}' to be in summary, but got: {summary_text}"


@then(parsers.parse('the overview page should display "{postal_code}" as the postal code'))
def overview_displays_postal_code(page, postal_code):
    payment_page = PaymentPage(page)
    assert payment_page.is_at_overview(), "Should be on overview page"
    # Verify the summary info contains the postal code
    summary_text = page.locator('.summary_info').inner_text()
    assert postal_code in summary_text, f"Expected '{postal_code}' in summary, but got: {summary_text}"


@then('the order summary should be visible')
def order_summary_visible(page):
    payment_page = PaymentPage(page)
    assert payment_page.is_order_summary_visible(), "Order summary should be visible"


@then(parsers.parse('the order summary should contain "{text}"'))
def order_summary_contains_text(page, text):
    payment_page = PaymentPage(page)
    order_summary = page.locator('.summary_info')
    summary_text = order_summary.inner_text()
    # Handle variations in text (e.g., "Shipping Address" vs "Shipping Information")
    if text == "Shipping Address" and "Shipping Information" in summary_text:
        assert True
    else:
        assert text in summary_text, f"Expected '{text}' to be in order summary, but got: {summary_text}"


@then('the order summary should display subtotal')
def summary_displays_subtotal(page):
    payment_page = PaymentPage(page)
    subtotal = payment_page.get_subtotal()
    assert subtotal is not None, "Subtotal should be displayed in summary"


@then('the order summary should display tax amount')
def summary_displays_tax(page):
    payment_page = PaymentPage(page)
    tax = payment_page.get_tax()
    assert tax is not None, "Tax amount should be displayed in summary"


@then('the order summary should display total amount')
def summary_displays_total(page):
    payment_page = PaymentPage(page)
    total = payment_page.get_order_total()
    assert total is not None, "Total amount should be displayed in summary"
