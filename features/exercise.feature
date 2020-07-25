Feature: fizz buzz

  Scenario Outline: fizz
    Given I have a positive integer <i>
    When the integer is a multiple of 3 or contains 3 <b>
    Then I should print Fizz

    Examples: fizz
      | i  | b |
      | 3  | 1 |
      | 5  | 0 |
      | 6  | 1 |
      | 13 | 1 |

  Scenario Outline: buzz
    Given I have a positive integer <i>
    When the integer is a multiple of 5 or contains 5 <b>
    Then I should print Buzz

    Examples: buzz
      | i  | b |
      | 3  | 0 |
      | 5  | 1 |
      | 6  | 0 |
      | 51 | 1 |
