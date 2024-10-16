Feature: Update contact

    As a user
    I can update a contact
    to have it reflect changes.

    Scenario: User changes first name
        Given a user
        And a contact
        When she posts a changed first name "Joe"
        Then the first name of this contact is "Joe"

    Scenario: User changes last name
        Given a user
        And a contact
        When she posts a changed last name "Bloggs"
        Then the last name of this contact is "Bloggs"

    Scenario: User changes e-mail
        Given a user
        And a contact
        When she posts a changed e-mail "joe.bloggs@example.com"
        Then the e-mail of this contact is "joe.bloggs@example.com"

    Scenario: User changes phone
        Given a user
        And a contact
        When she posts a changed phone "+44-011-755-5555"
        Then the phone of this contact is "+44-011-755-5555"

    Scenario: User changes address
        Given a user
        And a contact
        When she posts a changed address "Bristol"
        Then the address of this contact is "Bristol"
