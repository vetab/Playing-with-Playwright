import os
from dotenv import load_dotenv
import pytest
from playwright.sync_api import Playwright

load_dotenv()


@pytest.fixture
def login_page(playwright):
    """Create a browser/context/page and return the LoginPage wrapper.

    This fixture mirrors the existing tests' pattern so steps can reuse
    the same interactions and teardown behavior.
    """
    from src.pages.login import LoginPage

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Start tracing so feature tests keep parity with existing tests
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    login = LoginPage(page)

    yield login

    # Stop tracing and cleanup
    trace_path = os.getenv("BDD_TRACE_PATH", "evidence/trace_bdd.zip")
    context.tracing.stop(path=trace_path)
    context.close()
    browser.close()