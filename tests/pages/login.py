from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_button = page.locator("id=login-button")
        self.username = page.locator("id=user-name")
        self.password = page.locator("id=password")
        self.error_message = page.locator("data-test=error")

    def navigate(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()