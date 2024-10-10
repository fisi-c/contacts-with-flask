Feature: List contacts

    As a user
    I can view a list of all saved contacts
    so I know about the stored contacts.

    Scenario: User requests list
        Given a user
        And a number of contacts
        When she requests the contact list
        Then she sees a list of all contacts
        Then she sees the latest contact first in the list
