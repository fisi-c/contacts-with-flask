from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from contacts.db import get_db


bp = Blueprint('manage', __name__)


@bp.route('/')
def index():
    db = get_db()
    contacts = db.execute(
        'SELECT id, first_name, last_name, e_mail, phone_number, address, created_at'
        ' FROM contacts'
        ' ORDER BY created_at DESC'
    ).fetchall()
    return render_template('manage/index.html', contacts=contacts)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        e_mail = request.form['e_mail']
        phone_number = request.form['phone_number']
        address = request.form['address']
        error = None

        if not first_name:
            error = 'First name is required.'
        if not last_name:
            error = 'Last name is required.'
        if not e_mail:
            error = 'E-mail is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO contacts (first_name, last_name, e_mail, phone_number, address)'
                ' VALUES (?, ?, ?, ?, ?)',
                (first_name, last_name, e_mail, phone_number, address)
            )
            db.commit()
            return redirect(url_for('manage.index'))

    return render_template('manage/create.html')


def get_contact(id):
    contact = get_db().execute(
        'SELECT id, first_name, last_name, e_mail, phone_number, address, created_at'
        ' FROM contacts'
        ' WHERE id = ?',
        (id,)
    ).fetchone()

    if contact is None:
        abort(404, f"Contact id {id} doesn't exist.")

    return contact


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):
    contact = get_contact(id)

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        e_mail = request.form['e_mail']
        phone_number = request.form['phone_number']
        address = request.form['address']
        error = None

        if not first_name:
            error = 'First name is required.'
        if not last_name:
            error = 'Last name is required.'
        if not e_mail:
            error = 'E-mail is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE contacts SET first_name = ?, last_name = ?, e_mail = ?, phone_number = ?, address = ?'
                ' WHERE id = ?',
                (first_name, last_name, e_mail, phone_number, address, id,)
            )
            db.commit()
            return redirect(url_for('manage.index'))

    return render_template('manage/update.html', contact=contact)


@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    get_contact(id)
    db = get_db()
    db.execute('DELETE FROM contacts WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('manage.index'))
    