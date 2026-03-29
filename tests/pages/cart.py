from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.continue_shopping_button = page.locator("id=continue-shopping")
        self.checkout_button = page.locator("id=checkout")
        self.cart_items = page.locator(".cart_item")

    def is_at_cart_page(self):
        # The cart page URL is typically '/cart.html' on SauceDemo
        return self.page.url.endswith("/cart.html")

    def is_continue_shopping_visible(self):
        return self.continue_shopping_button.is_visible()

    def remove_item(self, item_name):
        # Assumes remove button has a data-test attribute with item name or similar
        self.page.locator(f'button[data-test="remove-{item_name.lower().replace(" ", "-")}"]').click()

    def is_empty(self):
        return self.cart_items.count() == 0

    def click_button(self, button_text):
        if button_text == "Continue Shopping":
            self.continue_shopping_button.click()
        elif button_text == "Checkout":
            self.checkout_button.click()

    def is_at_checkout(self):
        return "/checkout" in self.page.url
    
    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.page.locator('input[data-test="firstName"]').fill(first_name)
        self.page.locator('input[data-test="lastName"]').fill(last_name)
        self.page.locator('input[data-test="postalCode"]').fill(postal_code)
        self.page.locator('input[data-test="continue"]').click()

    def continue_to_overview(self):
        # Already handled by fill_checkout_info, but keep for clarity if needed
        pass

    def is_item_in_summary(self, item_name):
        # On the overview page, items are listed with class .inventory_item_name
        return self.page.locator(f'.inventory_item_name:text-is("{item_name}")').is_visible()

    def finish_checkout(self):
        self.page.locator('button[data-test="finish"]').click()

    def is_checkout_complete_displayed(self, message):
        # Now check for the title 'Checkout: Complete!' on the checkout-complete page
        title = self.page.locator('.title')
        title.wait_for(state='visible', timeout=5000)
        actual = ' '.join(title.inner_text().split())
        expected = ' '.join(message.split())
        return actual == expected
        