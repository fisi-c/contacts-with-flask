Feature: Update contact

    As a user
    I can update a contact
    to have it reflect changes.

    Scenario: User changes first name
        Given a user
        And a contact
        When she posts a changed first name
        Then the changed first name is in the database

    Scenario: User changes last name
        Given a user
        And a contact
        When she posts a changed last name
        Then the changed last name is in the database

    Scenario: User changes e-mail
        Given a user
        And a contact
        When she posts a changed e-mail "changed@example.com"
        Then the e-mail in the database is "changed@example.com"

    Scenario: User changes phone
        Given a user
        And a contact
        When she posts a changed phone "+49666600000"
        Then the phone in the database is "+49666600000"

    Scenario: User changes address
        Given a user
        And a contact
        When she posts a changed address "somewhereoverthemountain"
        Then the changed address is in the database "somewhereoverthemountain"
