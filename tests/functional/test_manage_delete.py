"""Delete contact feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from contacts.db import get_db


@scenario('features/manage/delete.feature', 'User deletes contact')
def test_user_deletes_contact():
    """User deletes contact."""


@given('a contact')
def _(app):
    """a contact."""
    with app.app_context():
        db = get_db()
        db.execute(
            "INSERT INTO contacts (first_name, last_name, e_mail, phone_number, address, created_at)"
            "VALUES ('Joe', 'Bloggs', 'joe.bloggs@example.com', '+44-011-755-5555', 'Bristol', '2024-01-01 00:00:00');"
        )


@given('a user')
def _():
    """a user."""
    pass


@when('she posts deleting the contact')
def _(client):
    """she posts deleting the contact."""
    client.post('/1/delete')


@then('there is no contact in the database')
def _(app):
    """there is no contact in the database."""
    with app.app_context():
        db = get_db()
        contact = db.execute('SELECT * FROM contacts WHERE id = 1').fetchone()
        assert contact is None