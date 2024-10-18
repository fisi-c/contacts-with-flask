Feature: Delete contact

    As a user
    I can delete a contact
    to have it removed permanently.

    Scenario: User deletes contact
        Given a user
        And one contact
        When she posts deleting the contact with id 1
        Then there is no contact with id 1 in the database
