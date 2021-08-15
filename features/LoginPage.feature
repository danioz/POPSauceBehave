Feature: SauceDemo Login

  Scenario: Login to SauceDemo with valid parameters
    Given I am on SauceDemo LoginPage
    When I enter username "standard_user" and password "secret_sauce"
    And I click on login button
    Then I must be successfully login to the Inventory page


  Scenario Outline: Login to SauceDemo with Multiple parameters
    Given I am on SauceDemo LoginPage
    When I enter username "<username>" and password "<password>"
    And I click on login button
    Then System must display "<error_message>"

    Examples:
      | username        | password     | error_message                                                             |
      | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out.                       |
      | user            | password     | Epic sadface: Username and password do not match any user in this service |