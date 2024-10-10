"""Add contact feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/contact_add.feature', 'User omits e-mail')
def test_user_omits_email():
    """User omits e-mail."""


@scenario('features/contact_add.feature', 'User omits first name')
def test_user_omits_first_name():
    """User omits first name."""


@scenario('features/contact_add.feature', 'User omits last name')
def test_user_omits_last_name():
    """User omits last name."""


@scenario('features/contact_add.feature', 'User submits new contact')
def test_user_submits_new_contact():
    """User submits new contact."""


@given('a user')
def _():
    """a user."""
    raise NotImplementedError


@when('she posts a contact')
def _():
    """she posts a contact."""
    raise NotImplementedError


@when('she posts a contact without e-mail')
def _():
    """she posts a contact without e-mail."""
    raise NotImplementedError


@when('she posts a contact without first name')
def _():
    """she posts a contact without first name."""
    raise NotImplementedError


@when('she posts a contact without last name')
def _():
    """she posts a contact without last name."""
    raise NotImplementedError


@then('she can see an error message')
def _():
    """she can see an error message."""
    raise NotImplementedError


@then('the contact is in the database')
def _():
    """the contact is in the database."""
    raise NotImplementedError


@then('the contact is not in the database')
def _():
    """the contact is not in the database."""
    raise NotImplementedError

