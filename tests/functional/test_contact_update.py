"""Update contact feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/contact_update.feature', 'User changes address')
def test_user_changes_address():
    """User changes address."""


@scenario('features/contact_update.feature', 'User changes e-mail')
def test_user_changes_email():
    """User changes e-mail."""


@scenario('features/contact_update.feature', 'User changes first name')
def test_user_changes_first_name():
    """User changes first name."""


@scenario('features/contact_update.feature', 'User changes last name')
def test_user_changes_last_name():
    """User changes last name."""


@scenario('features/contact_update.feature', 'User changes phone')
def test_user_changes_phone():
    """User changes phone."""


@given('a contact')
def _():
    """a contact."""
    raise NotImplementedError


@given('a user')
def _():
    """a user."""
    raise NotImplementedError


@when('she posts a changed address "somewhereoverthemountain"')
def _():
    """she posts a changed address "somewhereoverthemountain"."""
    raise NotImplementedError


@when('she posts a changed e-mail "changed@example.com"')
def _():
    """she posts a changed e-mail "changed@example.com"."""
    raise NotImplementedError


@when('she posts a changed first name')
def _():
    """she posts a changed first name."""
    raise NotImplementedError


@when('she posts a changed last name')
def _():
    """she posts a changed last name."""
    raise NotImplementedError


@when('she posts a changed phone "+49666600000"')
def _():
    """she posts a changed phone "+49666600000"."""
    raise NotImplementedError


@then('the changed address is in the database "somewhereoverthemountain"')
def _():
    """the changed address is in the database "somewhereoverthemountain"."""
    raise NotImplementedError


@then('the changed first name is in the database')
def _():
    """the changed first name is in the database."""
    raise NotImplementedError


@then('the changed last name is in the database')
def _():
    """the changed last name is in the database."""
    raise NotImplementedError


@then('the e-mail in the database is "changed@example.com"')
def _():
    """the e-mail in the database is "changed@example.com"."""
    raise NotImplementedError


@then('the phone in the database is "+49666600000"')
def _():
    """the phone in the database is "+49666600000"."""
    raise NotImplementedError

