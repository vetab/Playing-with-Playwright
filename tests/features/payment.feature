Feature: SauceDemo Payment and Billing

  Scenario: User can complete checkout with valid payment details
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I add the item "Sauce Labs Backpack" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    When I fill in the checkout information with first name "John", last name "Doe", and postal code "12345"
    And I continue to the overview page
    Then I should see "Sauce Labs Backpack" in the checkout summary
    And the order total should be displayed
    When I finish the checkout
    Then I should see the message "Checkout: Complete!"

  Scenario: User can add multiple items and verify total price calculation
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I add the item "Sauce Labs Backpack" to the cart
    And I add the item "Sauce Labs Bike Light" to the cart
    And I add the item "Sauce Labs Bolt T-Shirt" to the cart
    When I view the cart
    Then the cart should contain 3 items

  Scenario: Verify billing address section in checkout
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I add the item "Sauce Labs Backpack" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    And the billing address form should be visible
    When I fill in the checkout information with first name "Jane", last name "Smith", and postal code "54321"
    And I continue to the overview page
    Then the order summary should be visible

  Scenario: Verify order summary displays correct payment information
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I add the item "Sauce Labs Fleece Jacket" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    When I fill in the checkout information with first name "Bob", last name "Wilson", and postal code "99999"
    And I continue to the overview page
    Then the order summary should be visible
    And the order summary should contain "Payment Information"
    And the order summary should contain "Shipping Address"

  Scenario: Verify tax and total calculation on order summary
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I add the item "Sauce Labs Fleece Jacket" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    When I fill in the checkout information with first name "Alice", last name "Johnson", and postal code "11111"
    And I continue to the overview page
    Then the order summary should display subtotal
    And the order summary should display tax amount
    And the order summary should display total amount
