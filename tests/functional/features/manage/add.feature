Feature: Add contact

    As a user
    I can add a new contact
    to have it stored permanently.

    Scenario: User submits new contact
        Given a user
        When she posts a contact
        Then a contact is in the database

    Scenario: User omits first name
        Given a user
        When she posts a contact without first name
        Then she can see an error message
        And there is no contact in the database

    Scenario: User omits last name
        Given a user
        When she posts a contact without last name
        Then she can see an error message
        And there is no contact in the database

    Scenario: User omits e-mail
        Given a user
        When she posts a contact without e-mail
        Then she can see an error message
        And there is no contact in the database
