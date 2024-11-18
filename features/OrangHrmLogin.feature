Feature: OrangeHrm Login

  Scenario: Login to orangeHrm with valid parameters
    Given I launch chrome browser
    When  I open orangeHrm Homepage
    And Enter username "Admin" and password "admin123 "
    And Click on login button
    Then User must successfully login to the Dashboard page

  Scenario Outline: Login to orangeHrm with multiple parameters
    Given I launch chrome browser
    When  I open orangeHrm Homepage
    And Enter username "<username>" and password "<password> "
    And Click on login button
    Then User must successfully login to the Dashboard page
    Examples:
      | username | password |
      | Admin    | admin123 |
      | admin123 | Admin    |
      | adminxyz | admin123 |
      | mahesh   | ram mahi |
      | Admin    | adminxyz |
