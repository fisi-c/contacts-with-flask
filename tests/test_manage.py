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
def test_returns_404_for_nonexisting_contact(client, path):
    assert client.post(path).status_code == 404


def test_delete_post_method_redirects_to_index(client):
    response = client.post('/1/delete')
    assert response.headers['Location'] == '/'
