from playwright.sync_api import Page


class PaymentPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        # Checkout info fields
        self.first_name_field = page.locator('input[data-test="firstName"]')
        self.last_name_field = page.locator('input[data-test="lastName"]')
        self.postal_code_field = page.locator('input[data-test="postalCode"]')
        self.continue_button = page.locator('input[data-test="continue"]')
        
        # Overview page elements
        self.order_summary = page.locator('.summary_info')
        self.subtotal = page.locator('.summary_subtotal_label')
        self.tax = page.locator('.summary_tax_label')
        self.total = page.locator('.summary_total_label')
        self.payment_info = page.locator('.summary_info_label:has-text("Payment Information")')
        self.shipping_info = page.locator('.summary_info_label:has-text("Shipping Address")')
        
        # Billing info display
        self.billing_name = page.locator('.summary_info')
        self.billing_postal_code = page.locator('.summary_info')
        
        # Finish button
        self.finish_button = page.locator('button[data-test="finish"]')

    def is_at_checkout(self):
        return self.page.url.endswith("/checkout-step-one.html")

    def is_at_overview(self):
        return self.page.url.endswith("/checkout-step-two.html")

    def fill_billing_info(self, first_name, last_name, postal_code):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.postal_code_field.fill(postal_code)
        self.continue_button.click()
        self.page.wait_for_url("**/checkout-step-two.html")

    def get_order_total(self):
        """Extract and return the total amount from the order summary"""
        total_text = self.total.inner_text()
        # Extract numeric value from "Total: $XX.XX"
        return total_text.split('$')[-1].strip() if '$' in total_text else None

    def get_subtotal(self):
        """Extract and return the subtotal amount"""
        subtotal_text = self.subtotal.inner_text()
        return subtotal_text.split('$')[-1].strip() if '$' in subtotal_text else None

    def get_tax(self):
        """Extract and return the tax amount"""
        tax_text = self.tax.inner_text()
        return tax_text.split('$')[-1].strip() if '$' in tax_text else None

    def is_order_summary_visible(self):
        return self.order_summary.is_visible()

    def is_payment_info_visible(self):
        return self.payment_info.is_visible()

    def is_shipping_info_visible(self):
        return self.shipping_info.is_visible()

    def get_billing_name(self):
        """Get the billing name displayed on overview page"""
        return self.billing_name.inner_text() if self.billing_name.is_visible() else None

    def get_billing_postal_code(self):
        """Get the billing postal code displayed on overview page"""
        return self.billing_postal_code.inner_text() if self.billing_postal_code.is_visible() else None

    def finish_checkout(self):
        self.finish_button.click()
        self.page.wait_for_url("**/checkout-complete.html")

    def contains_text(self, element_locator, text):
        """Check if an element contains specific text"""
        return text in element_locator.inner_text()
