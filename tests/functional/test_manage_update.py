"""Update contact feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from contacts.db import get_db


@scenario('features/manage/update.feature', 'User changes address')
def test_user_changes_address():
    """User changes address."""


@scenario('features/manage/update.feature', 'User changes e-mail')
def test_user_changes_email():
    """User changes e-mail."""


@scenario('features/manage/update.feature', 'User changes first name')
def test_user_changes_first_name():
    """User changes first name."""


@scenario('features/manage/update.feature', 'User changes last name')
def test_user_changes_last_name():
    """User changes last name."""


@scenario('features/manage/update.feature', 'User changes phone')
def test_user_changes_phone():
    """User changes phone."""


@given('a contact')
def _(app, anon_contact):
    """a contact."""
    with app.app_context():
        db = get_db()
        db.execute(
            "INSERT INTO contacts (first_name, last_name, e_mail)"
            " VALUES (?, ?, ?)",
            (anon_contact['first_name'], anon_contact['last_name'], anon_contact['e_mail'],)
        )
        db.commit()


@given('a user')
def _():
    """a user."""
    pass


@when('she posts a changed address "Bristol"')
def _(client, anon_contact):
    """she posts a changed address "Bristol"."""
    anon_contact['address'] = 'Bristol'
    client.post('/1/update', data=anon_contact)


@when('she posts a changed e-mail "joe.bloggs@example.com"')
def _(client, anon_contact):
    """she posts a changed e-mail "joe.bloggs@example.com"."""
    anon_contact['e_mail'] = 'joe.bloggs@example.com'
    client.post('/1/update', data=anon_contact)


@when('she posts a changed first name "Joe"')
def _(client, anon_contact):
    """she posts a changed first name "Joe"."""
    anon_contact['first_name'] = 'Joe'
    client.post('/1/update', data=anon_contact)


@when('she posts a changed last name "Bloggs"')
def _(client, anon_contact):
    """she posts a changed last name "Bloggs"."""
    anon_contact['last_name'] = 'Bloggs'
    client.post('/1/update', data=anon_contact)


@when('she posts a changed phone "+44-011-755-5555"')
def _(client, anon_contact):
    """she posts a changed phone "+44-011-755-5555"."""
    anon_contact['phone_number'] = '+44-011-755-5555'
    client.post('/1/update', data=anon_contact)


@then('the address of this contact is "Bristol"')
def _(app):
    """the address of this contact is "Bristol"."""
    with app.app_context():
        db = get_db()
        contact = db.execute('SELECT * FROM contacts WHERE id = 1').fetchone()
        assert contact['address'] == 'Bristol'


@then('the first name of this contact is "Joe"')
def _(app):
    """the first name of this contact is "Joe"."""
    with app.app_context():
        db = get_db()
        contact = db.execute('SELECT * FROM contacts WHERE id = 1').fetchone()
        assert contact['first_name'] == 'Joe'


@then('the last name of this contact is "Bloggs"')
def _(app):
    """the last name of this contact is "Bloggs"."""
    with app.app_context():
        db = get_db()
        contact = db.execute('SELECT * FROM contacts WHERE id = 1').fetchone()
        assert contact['last_name'] == 'Bloggs'


@then('the e-mail of this contact is "joe.bloggs@example.com"')
def _(app):
    """the e-mail of this contact is "joe.bloggs@example.com"."""
    with app.app_context():
        db = get_db()
        contact = db.execute('SELECT * FROM contacts WHERE id = 1').fetchone()
        assert contact['e_mail'] == 'joe.bloggs@example.com'


@then('the phone of this contact is "+44-011-755-5555"')
def _(app):
    """the phone of this contact is "+44-011-755-5555"."""
    with app.app_context():
        db = get_db()
        contact = db.execute('SELECT * FROM contacts WHERE id = 1').fetchone()
        assert contact['phone_number'] == '+44-011-755-5555'
