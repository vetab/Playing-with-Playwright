from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page) -> None:
        self.page = page
        self.header_title = page.locator(".title")
        self.burger_button = page.locator("id=react-burger-menu-btn")
        self.all_items = page.locator("id=inventory_sidebar_link")
        self.logout = page.locator("id=logout_sidebar_link")
        self.reset_app_state = page.locator("id=reset_sidebar_link")
        self.shopping_cart = page.locator("id=shopping_cart_container")
        # self.a_to_z = page.select_option('data-test=product_sort_container', label = 'Name (A to Z)')
        # self.z_to_a = page.select_option('data-test=product_sort_container', label = 'Name (Z to A)')
        # self.price_low_to_high = page.select_option('data-test=product_sort_container', label = 'Price (low to high)')
        # self.price_high_to_low = page.select_option('data-test=product_sort_container', label = 'Price (high to low)')
        self.add_to_cart_backpack_button = page.locator("id=add-to-cart-sauce-labs-backpack")
        #self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.shopping_cart_badge = page.locator("//*[@id=\"shopping_cart_container\"]/a/span")

    def click_burger_button(self):
        self.burger_button.click()

    def add_backpack_item_to_cart(self):
        self.add_to_cart_backpack_button.click()

    def click_logout(self):
        self.logout.click()

