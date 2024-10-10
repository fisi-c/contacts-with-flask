"""Delete contact feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/contact_delete.feature', 'User deletes contact')
def test_user_deletes_contact():
    """User deletes contact."""


@given('a contact')
def _():
    """a contact."""
    raise NotImplementedError


@given('a user')
def _():
    """a user."""
    raise NotImplementedError


@when('she posts deleting the contact')
def _():
    """she posts deleting the contact."""
    raise NotImplementedError


@then('the contact is not in the database')
def _():
    """the contact is not in the database."""
    raise NotImplementedError

