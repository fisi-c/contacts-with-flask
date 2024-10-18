"""Add contact feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from contacts.db import get_db


@scenario('features/manage/add.feature', 'User omits e-mail')
def test_user_omits_email():
    """User omits e-mail."""


@scenario('features/manage/add.feature', 'User omits first name')
def test_user_omits_first_name():
    """User omits first name."""


@scenario('features/manage/add.feature', 'User omits last name')
def test_user_omits_last_name():
    """User omits last name."""


@scenario('features/manage/add.feature', 'User submits new contact')
def test_user_submits_new_contact():
    """User submits new contact."""


@given('a user')
def _():
    """a user."""
    pass


@when('she posts a contact')
def _(client, anon_contact):
    """she posts a contact."""
    client.post('/create', data=anon_contact)


@when('she posts a contact without e-mail', target_fixture='response')
def _(client, anon_contact):
    """she posts a contact without e-mail."""
    anon_contact['e_mail'] = ''
    return client.post('/create', data=anon_contact)


@when('she posts a contact without first name', target_fixture='response')
def _(client, anon_contact):
    """she posts a contact without first name."""
    anon_contact['first_name'] = ''
    return client.post('/create', data=anon_contact)


@when('she posts a contact without last name', target_fixture='response')
def _(client, anon_contact):
    """she posts a contact without last name."""
    anon_contact['last_name'] = ''
    return client.post('/create', data=anon_contact)


@then('she can see an error message')
def _(response):
    """she can see an error message."""
    assert b'is required.' in response.data


@then('a contact is in the database')
def _(app):
    """a contact is in the database."""
    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM contacts').fetchone()[0]
        assert count == 1


@then('there is no contact in the database')
def _(app):
    """there is no contact in the database."""
    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM contacts').fetchone()[0]
        assert not count
