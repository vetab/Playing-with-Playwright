
Feature: SauceDemo Shopping Cart

  Scenario: Remove an item from the cart
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I add the item "Sauce Labs Backpack" to the cart
    When I view the cart
    And I remove the item "Sauce Labs Backpack" from the cart
    Then the cart should be empty

  Scenario: User can continue shopping from cart
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I add the item "Sauce Labs Backpack" to the cart
    When I view the cart
    And I click the "Continue Shopping" button
    Then I should be redirected to the inventory page

  Scenario: User can checkout with an item in the cart
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I add the item "Sauce Labs Backpack" to the cart
    When I view the cart
    And I click the "Checkout" button
    Then the checkout page should be displayed
    When I fill in the checkout information with first name "John", last name "Doe", and postal code "12345"
    And I continue to the overview page
    Then I should see "Sauce Labs Backpack" in the checkout summary
    When I finish the checkout
    Then I should see the message "Checkout: Complete!"

