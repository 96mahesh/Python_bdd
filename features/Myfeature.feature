Feature: OrangeHrm Logo
  Scenario: Logo presence on OrangeHrm home page
    Given Launch chrome browser
    When Open Orange Hrm Home page
    Then verifythat the logo prasent on page
    And close browser