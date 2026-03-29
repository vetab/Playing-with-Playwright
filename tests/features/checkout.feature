Feature: SauceDemo Shopping Cart and Checkout

  As a shopper
  I want to manage items in my cart and complete the checkout process
  So that I can purchase products from the SauceDemo store

  Background:
    Given I am logged in as "standard_user" with password "secret_sauce"

  # Cart Management Scenarios
  Scenario: Add an item to cart and remove it
    Given I add the item "Sauce Labs Backpack" to the cart
    When I view the cart
    And I remove the item "Sauce Labs Backpack" from the cart
    Then the cart should be empty

  Scenario: Continue shopping from the cart
    Given I add the item "Sauce Labs Backpack" to the cart
    When I view the cart
    And I click the "Continue Shopping" button
    Then I should be redirected to the inventory page

  Scenario: Add multiple items to cart
    Given I add the item "Sauce Labs Backpack" to the cart
    And I add the item "Sauce Labs Bike Light" to the cart
    And I add the item "Sauce Labs Bolt T-Shirt" to the cart
    When I view the cart
    Then the cart should contain 3 items

  # Checkout Process Scenarios
  Scenario: Complete checkout with single item
    Given I add the item "Sauce Labs Backpack" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    When I fill in the checkout information with first name "John", last name "Doe", and postal code "12345"
    And I continue to the overview page
    Then I should see "Sauce Labs Backpack" in the checkout summary
    And the order total should be displayed
    When I finish the checkout
    Then I should see the message "Checkout: Complete!"

  Scenario: Verify billing address form is visible during checkout
    Given I add the item "Sauce Labs Backpack" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    And the billing address form should be visible

  Scenario: Complete checkout with multiple items
    Given I add the item "Sauce Labs Backpack" to the cart
    And I add the item "Sauce Labs Bike Light" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    When I fill in the checkout information with first name "Jane", last name "Smith", and postal code "54321"
    And I continue to the overview page
    Then the order summary should be visible

  # Order Summary and Payment Scenarios
  Scenario: Verify order summary displays payment and shipping information
    Given I add the item "Sauce Labs Fleece Jacket" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    When I fill in the checkout information with first name "Bob", last name "Wilson", and postal code "99999"
    And I continue to the overview page
    Then the order summary should be visible
    And the order summary should contain "Payment Information"
    And the order summary should contain "Shipping Address"

  Scenario: Verify order summary displays pricing breakdown
    Given I add the item "Sauce Labs Fleece Jacket" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    When I fill in the checkout information with first name "Alice", last name "Johnson", and postal code "11111"
    And I continue to the overview page
    Then the order summary should display subtotal
    And the order summary should display tax amount
    And the order summary should display total amount
