import pytest


def test_index_returns_all_fields(client):
    response = client.get('/')
    assert b'Joe' in response.data
    assert b'Bloggs' in response.data
    assert b'joe.bloggs@example.com' in response.data
    assert b'+44-011-755-5555' in response.data
    assert b'Bristol' in response.data
    assert b'href="/1/update"' in response.data


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_returns_404_for_nonexistant_contact(client, path):
    assert client.post(path).status_code == 404


@pytest.mark.parametrize('path', (
    '/1/update',
))
def test_update_post_method_validates_input(client, path):
    response = client.post(path, data={
        'first_name': '',
        'last_name': 'Anonymous',
        'e_mail': 'anonymous@example.com',
        'phone_number': '',
        'address': '',
    })
    assert b'First name is required.' in response.data

    response = client.post(path, data={
        'first_name': 'Anonymous',
        'last_name': '',
        'e_mail': 'anonymous@example.com',
        'phone_number': '',
        'address': '',
    })
    assert b'Last name is required.' in response.data

    response = client.post(path, data={
        'first_name': 'Anonymous',
        'last_name': 'Anonymous',
        'e_mail': '',
        'phone_number': '',
        'address': '',
    })
    assert b'E-mail is required.' in response.data


def test_delete_post_method_redirects_to_index(client):
    response = client.post('/1/delete')
    assert response.headers["Location"] == "/"
    