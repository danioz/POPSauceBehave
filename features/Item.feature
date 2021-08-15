Feature: Adding and removing items to/from cart at item page

  Background: common steps
    Given I am on SauceDemo LoginPage
    When  I login with valid username and password
    Then  I should be on Inventory Page

  Scenario Outline: Adding item to cart at item page
    When  I click at "<item>" title at Inventory page
    Then  I should be at Item page
    When  I click add to cart button at item page
    Then  Cart icon should display 1

    Examples:
      | item                              |
      | Sauce Labs Backpack               |
      | Sauce Labs Bike Light             |
      | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Fleece Jacket          |
      | Sauce Labs Onesie                 |
      | Test.allTheThings() T-Shirt (Red) |

  Scenario Outline: Removing item from cart at item page
    When  I click at "<item>" title at Inventory page
    Then  I should be at Item page
    When  I click add to cart button at item page
    Then  Cart icon should display 1
    When  I click remove button at item page
    Then  Cart should be empty

    Examples:
      | item                              |
      | Sauce Labs Backpack               |
      | Sauce Labs Bike Light             |
      | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Fleece Jacket          |
      | Sauce Labs Onesie                 |
      | Test.allTheThings() T-Shirt (Red) |

  Scenario Outline: Verifying name, description and price of item
    When  I check name of the "<item>" at Inventory page
    And   I check description of the "<item>" at Inventory page
    And   I check price of "<item>" at Inventory page
    And   I click at "<item>" title at Inventory page
    Then  I should be at Item page
    And   Name of "<item>" should match at Item page
    And   Description of "<item>" should match at Item page
    And   Price of "<item>" should match at Item page

    Examples:
      | item                              |
      | Sauce Labs Backpack               |
      | Sauce Labs Bike Light             |
      | Sauce Labs Bolt T-Shirt           |
      | Sauce Labs Fleece Jacket          |
      | Sauce Labs Onesie                 |
      | Test.allTheThings() T-Shirt (Red) |
