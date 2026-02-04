Feature: SauceDemo Shopping Cart

  Scenario: Successful login and view inventory
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the inventory page

  Scenario: Add an item to the cart
    Given I am logged in as "standard_user" with password "secret_sauce"
    When I add the item "Sauce Labs Backpack" to the cart
    Then the cart badge should show "1"

  Scenario: Remove an item from the cart
    Given I have "Sauce Labs Backpack" in my cart
    When I remove the item "Sauce Labs Backpack" from the cart
    Then the cart badge should not be visible