from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.header_title = page.locator(".title")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")

    def is_at(self):
        return self.page.url.endswith("/inventory.html") and self.header_title.inner_text() == "Products"

    def add_to_cart(self, item_name):
        # item_name example: "Sauce Labs Backpack"
        item_id = self._item_id_from_name(item_name)
        add_btn = self.page.locator(f"#add-to-cart-{item_id}")
        add_btn.click()

    def remove_from_cart(self, item_name):
        item_id = self._item_id_from_name(item_name)
        remove_btn = self.page.locator(f"#remove-{item_id}")
        remove_btn.click()

    def get_cart_count(self):
        if self.shopping_cart_badge.is_visible():
            return int(self.shopping_cart_badge.inner_text())
        return 0

    def is_cart_badge_visible(self):
        return self.shopping_cart_badge.is_visible()

    def _item_id_from_name(self, item_name):
        # Converts item name to id format used in buttons
        # "Sauce Labs Backpack" -> "sauce-labs-backpack"
        return item_name.lower().replace(" ", "-")

