"""List contacts feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from contacts.db import get_db


@scenario('features/contact_list.feature', 'User requests list')
def test_user_requests_list():
    """User requests list."""


@given('a number of contacts')
def _(app):
    """a number of contacts."""
    with app.app_context():
        db = get_db()
        db.execute(
            "INSERT INTO contacts (first_name, last_name, e_mail, created_at)"
            "VALUES"
            "('Alpha', 'Anonymous', 'alpha@example.com', '2024-01-01 00:00:00'),"
            "('Beta', 'Anonymous', 'beta@example.com', '2024-01-02 00:00:00'),"
            "('Gamma', 'Anonymous', 'gamma@example.com', '2024-01-03 00:00:00');"
        )
        db.commit()


@given('a user')
def _():
    """a user."""
    pass


@when('she requests the contact list')
def _(client):
    """she requests the contact list."""
    global response
    response = client.get('/')


@then('she sees a list of all contacts')
def _():
    """she sees a list of all contacts."""
    global response
    assert b'Alpha' in response.data
    assert b'Beta' in response.data
    assert b'Gamma' in response.data


@then('she sees the latest contact first in the list')
def _():
    """she sees the latest contact first in the list."""
    global response
    _index = response.data.index
    assert _index(b'Gamma') < _index(b'Alpha')
    assert _index(b'Gamma') < _index(b'Beta')
