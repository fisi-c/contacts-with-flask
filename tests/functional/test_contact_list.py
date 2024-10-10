"""List contacts feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/contact_list.feature', 'User requests list')
def test_user_requests_list():
    """User requests list."""


@given('a number of contacts')
def _():
    """a number of contacts."""
    raise NotImplementedError


@given('a user')
def _():
    """a user."""
    raise NotImplementedError


@when('she requests the contact list')
def _():
    """she requests the contact list."""
    raise NotImplementedError


@then('she sees a list of all contacts')
def _():
    """she sees a list of all contacts."""
    raise NotImplementedError


@then('she sees the latest contact first in the list')
def _():
    """she sees the latest contact first in the list."""
    raise NotImplementedError

