Feature: Adding and removing items to/from cart

Background: common steps
    Given I am on SauceDemo LoginPage
    When I login with valid username and password
    Then I should be on Inventory Page

  Scenario: Adding item to cart
    When  I click add to cart button
    Then Cart icon should display 1

  Scenario: Adding 2 items to cart
    When  I click add to cart button
    And  I click add to cart button
    Then Cart icon should display 2

  Scenario: Removing item from cart
    When  I click add to cart button
    And I click remove button
    Then Cart icon should be empty

  Scenario Outline: Login to SauceDemo with Multiple parameters
    When I click add to cart button for item "<item>"
    Then Cart icon should display 1
    When I click remove button for item "<item>"
    Then Cart icon should be empty

    Examples:
      | item          |
      | backpack      |
      | bike-light    |
      | bolt-t-shirt  |
      | fleece-jacket |
      | onesie        |
      | t-shirt-(red) |




