Feature: Delete contact

    As a user
    I can delete a contact
    to have it removed permanently.

    Scenario: User deletes contact
        Given a user
        And a contact
        When she posts deleting the contact
        Then the contact is not in the database
