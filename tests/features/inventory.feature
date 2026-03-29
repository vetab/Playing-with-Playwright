Feature: SauceDemo Inventory Management

  As a shopper
  I want to browse products and manage my cart from the inventory page
  So that I can add items to my cart and proceed to checkout

  Scenario: Navigate to inventory after successful login
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the inventory page

  Scenario: Add item to cart and verify cart badge updates
    Given I am logged in as "standard_user" with password "secret_sauce"
    When I add the item "Sauce Labs Backpack" to the cart
    Then the cart badge should show "1"

  Scenario: Remove item from cart and verify cart badge is hidden
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I add the item "Sauce Labs Backpack" to the cart
    When I remove the item "Sauce Labs Backpack" from the cart
    Then the cart badge should not be visible