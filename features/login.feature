Feature: Validate login scenario of Facebook

  Background:
    Given The Facebook login page is loaded
  @login @login_with_valid_email
  Scenario Outline: Login Validation with Valid Email Scenarios
    Given The user and test details for login
    | TestCaseId   | TestCaseName     |
    | <TestCaseId> | <TestCaseName>   |
    When the user attempts to login with "<Email>" and "<Password>"
    | Email                      | Password      |
    | <Email>                    | <Password>    |
    Then the user should get a "<content>"
    | content          |
    | <content>        |

    Examples:
      | TestCaseId | TestCaseName                                   | Email                      | Password      | content                                          |
      | Login-001  | LOGIN - Valid Email, Invalid Password          | johncena92424@gmail.com    | Loki@96067832 | The password you've entered is incorrect        |
      | Login-002  | LOGIN - Valid Email, Valid Password            | johncena92424@gmail.com    | Loki@9606     | Welcome to Facebook                              |

  @login @login_with_invalid_email
    @login_with_invalid_email_format
  Scenario Outline: Login Validation with Invalid Email Scenarios
    Given The user and test details for login
    | TestCaseId | TestCaseName                                   |
    | <TestCaseId> | <TestCaseName>                               |
    When the user attempts to login with "<Email>" and "<Password>"
    | Email                      | Password      |
    | <Email>                    | <Password>    |
    Then the user should get a "<content>"
      | content       |
      | <content>     |
    Examples:
      | TestCaseId | TestCaseName                                   | Email                      | Password      | content                                          |
      | Login-003  | LOGIN - Invalid Email, Valid Password          | johncenaddd92424@gmail.com | Loki@9606     | The email address you entered isn't connected to an account. |
      | Login-004 | LOGIN - Invalid Email Format, Valid Password   | johncena92424gmail@.com    | Loki@9606     | We couldn't find an account that matches what you entered, but we've found one that closely matches. |

  @login @login_with_valid_phone
  Scenario Outline: Login Validation with Valid Phone Scenarios
    Given The user and test details for login
    | TestCaseId   | TestCaseName       |
    | <TestCaseId> | <TestCaseName>   |
    When the user attempts to login with phone "<Phone>" and "<Password>"
    | Phone                      | Password      |
    | <Phone>                    | <Password>    |
    Then the user should get a "<content>"
      | content      |
      | <content>    |
    Examples:
      | TestCaseId | TestCaseName                                   | Phone       | Password      | content                                          |
      | Login-005  | LOGIN - Valid Phone, Invalid Password          | 8105000676  | Loki@9606sdas | The password you've entered is incorrect.      |
      | Login-006  | LOGIN - Valid Phone, Valid Password            | 8105000676  | Loki@9606     | Welcome to Facebook                              |

  @login @login_with_invalid_phone
  Scenario Outline: Login Validation with Invalid Phone Scenarios
    Given The user and test details for login
    | TestCaseId   | TestCaseName    |
    | <TestCaseId> | <TestCaseName>  |
    When the user attempts to login with phone "<Phone>" and "<Password>"
    | Phone                      | Password      |
    | <Phone>                    | <Password>    |
    Then the user should get a "<content>"
      | content    |
      | <content>  |
    Examples:
      | TestCaseId | TestCaseName                                   | Phone       | Password      | content                                          |
      | Login-007 | LOGIN - Invalid Phone, Valid Password          | 8105000456  | Loki@9606     | The password you've entered is incorrect.      |

  @login @login_with_empty_password
    @login_with_empty_phone/email
  Scenario Outline: Login Validation with empty password Scenarios
    Given The user and test details for login
    | TestCaseId   | TestCaseName    |
    | <TestCaseId> | <TestCaseName>  |
    When the user attempts to login with "<data>"
    | data                      |
    | <data>                    |
    Then the user should get a "<content>"
      | content    |
      | <content>  |
    Examples:
      | TestCaseId | TestCaseName                                   | data                          | content                                          |
      | Login-008  | LOGIN - Valid Phone, Empty Password            | 81050000676                   | The email address or mobile number you entered isn't connected to an account. Find your account and log in. |
      | Login-009  | LOGIN - Valid Email, Empty Password            | johncena@92424gmail.com       | We couldn't find an account that matches what you entered, but we've found one that closely matches. |

    @login_with_empty_fields
  Scenario Outline: Login Validation with empty filed Scenario
    Given The user and test details for login
    | TestCaseId   | TestCaseName    |
    | <TestCaseId> | <TestCaseName>  |
    When the user attempts to login with empty fields
    Then the user should get a "<content>"
      | content    |
      | <content>  |
      Examples:
      | TestCaseId | TestCaseName                                     | content                     |
      | Login-010  | LOGIN - Empty Email/Phone, Empty Password        | The email address or mobile number you entered isn't connected to an account. Find your account and log in. |
