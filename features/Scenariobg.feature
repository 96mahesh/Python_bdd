Feature: OrangeHrm Login

  Scenario: Login to Hrm Application
    Given I launch Browser
    When I Open application
    And Enter valid username and password
    And click on login
    Then User must login to the Dashboard Page

  Scenario: Search user
    Given I launch Browser
    When I Open application
    And Enter valid username and password
    And click on login
    When navigate to seacrh Page
    Then Search Page should be display

  Scenario: Advance Search user
    Given I launch Browser
    When I Open application
    And Enter valid username and password
    And click on login
    When navigate to Advance seacrh Page
    Then Advance Page should be display