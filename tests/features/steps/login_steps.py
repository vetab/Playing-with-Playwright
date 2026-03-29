import os
import pytest
from pytest_bdd import given, when, then, parsers
from playwright.sync_api import expect
from dotenv import load_dotenv

from tests.pages.login import LoginPage
from tests.pages.inventory import InventoryPage

# Load environment variables from .env file if it exists
load_dotenv()

# Get environment variables with fallback defaults
ROOT_URL = os.getenv('ROOT_URL', 'https://www.saucedemo.com')
STANDARD_USER = os.getenv('STANDARD_USER', 'standard_user')
LOCKED_OUT_USER = os.getenv('LOCKED_OUT_USER', 'locked_out_user')
PASSWORD = os.getenv('PASSWORD', 'secret_sauce')


@pytest.fixture
def login_page(page):
    return LoginPage(page)



@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@given('I am on the login page')
def i_am_on_login_page(login_page):
    login_page.navigate(ROOT_URL)

@then(parsers.parse('I should see "{expected}"'))
def i_should_see(login_page, inventory_page, expected):
    # For the success row the Examples table uses "Products page" 4 assert the header
    if expected == 'Products page':
        expect(inventory_page.header_title).to_have_text('Products')
    else:
        expect(login_page.error_message).to_have_text(expected)

def _resolve_username(name: str) -> str:
    """Map placeholder names to environment values where appropriate."""
    if name == 'standard_user':
        return os.getenv('STANDARD_USER', 'standard_user')
    if name == 'locked_out_user':
        return os.getenv('LOCKED_OUT_USER', 'locked_out_user')
    return name


def _resolve_password(name: str) -> str:
    if name == 'password':
        return os.getenv('PASSWORD', 'secret_sauce')
    return name


@when('I click the login button')
def click_login(login_page):
    login_page.login_click()


@when(parsers.parse('I enter username "{username}"'))
def enter_username(login_page, username):
    login_page.enter_username(_resolve_username(username))


@when(parsers.re(r'I login with "(?P<username>.*)" and "(?P<password>.*)"'))
def login_with(login_page, username, password):
    user = _resolve_username(username)
    pwd = _resolve_password(password)
    # If both values are empty strings, submit empty values to trigger validation
    login_page.login(user or "", pwd or "")


# Note: 'I should see "<expected>"' is handled by `i_should_see` above.


@then('I should be on the products page')
def should_be_on_products_page(login_page):
    from tests.pages.inventory import InventoryPage

    inventory = InventoryPage(login_page.page)
    expect(inventory.header_title).to_have_text('Products')

