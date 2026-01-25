import os

from playwright.sync_api import expect, Playwright
from src.pages.login import LoginPage
from dotenv import load_dotenv

from src.pages.inventory import InventoryPage

load_dotenv()

STANDARD_USER = os.getenv('STANDARD_USER')
PASSWORD = os.getenv('PASSWORD')
ROOT_URL = os.getenv('ROOT_URL')


def test_add_one_item_to_cart(playwright:Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate(ROOT_URL)

    login_page.submit_login(STANDARD_USER, PASSWORD)

    expect(inventory_page.header_title).to_have_text("Products")

    inventory_page.add_backpack_item_to_cart()
    expect(inventory_page.shopping_cart_badge).to_have_text("1")

    inventory_page.click_burger_button()
    inventory_page.click_logout()


    context.tracing.stop(path="evidence/trace_cart.zip")

    context.close()
    browser.close()