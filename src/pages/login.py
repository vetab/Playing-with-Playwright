from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_button = page.locator("id=login-button")
        self.username = page.locator("id=user-name")
        self.password = page.locator("id=password")
        self.error_message = page.locator("data-test=error")

    def navigate(self, web_url):
        self.page.goto(web_url)

    def submit_login(self, email, password):
        self.username.fill(email)
        self.password.fill(password)
        self.login_button.click()

    def enter_username(self, email_address):
        self.username.fill(email_address)

    def enter_password(self, user_password):
        self.password.fill(user_password)

    def login_click(self):
        self.login_button.click()