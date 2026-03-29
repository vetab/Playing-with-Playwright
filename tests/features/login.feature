Feature: SauceDemo User Authentication

  As a user
  I want to log in to the SauceDemo application
  So that I can access my account and view products

  Verify login error messages and successful login flow using a Scenario Outline.

  Scenario Outline: Login behaviour (errors and success)
    Given I am on the login page
    When I login with "<username>" and "<password>"
    Then I should see "<expected>"

  Examples:
    | username        | password         | expected                                                                 |
    |                 |                 | Epic sadface: Username is required                                       |
    | standard_user   |                 | Epic sadface: Password is required                                       |
    | locked_out_user | password        | Epic sadface: Sorry, this user has been locked out.                      |
    | invalid_user    | invalid_password | Epic sadface: Username and password do not match any user in this service |
    | standard_user   | password        | Products page                                                            |