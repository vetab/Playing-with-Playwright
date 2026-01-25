import os

from playwright.sync_api import expect, Playwright
from src.pages.login import LoginPage
from dotenv import load_dotenv

load_dotenv()

STANDARD_USER = os.getenv('STANDARD_USER')
LOCKED_OUT_USER = os.getenv('LOCKED_OUT_USER')
PASSWORD = os.getenv('PASSWORD')
ROOT_URL = os.getenv('ROOT_URL')


def test_wrong_user_password_error_messages(playwright: Playwright) -> None:
    # Set up an emulated device to run the tests
    galaxy_tab = playwright.devices['Galaxy Tab S4 landscape']

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        **galaxy_tab,
    )
    # Running context to capture screenshots after every step
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Open new page
    page = context.new_page()
    login_page = LoginPage(page)

    # Go to https://saucedemo.com/
    login_page.navigate(ROOT_URL)

    login_page.login_click()

    # Assert that the error messages are shown when no right values are present
    expect(login_page.error_message).to_have_text("Epic sadface: Username is required")

    login_page.enter_username(STANDARD_USER)
    login_page.login_click()

    expect(login_page.error_message).to_have_text("Epic sadface: Password is required")

    # Setup of a path where the screenshots will be saved and tracing stop
    context.tracing.stop(path="evidence/trace_errors.zip")

    context.close()
    browser.close()


def test_locked_user_error_message(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Running context to capture screenshots after every step
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    login_page = LoginPage(page)

    login_page.navigate(ROOT_URL)
    login_page.submit_login(LOCKED_OUT_USER, PASSWORD)
    login_page.login_click()

    expect(login_page.error_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")

    context.tracing.stop(path="evidence/trace_locked_user_error.zip")

    context.close()
    browser.close()