
import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200


def test_empty_url_rejected(client):
    response = client.post('/', data={
        'original_url': ''
    })
    assert response.status_code == 200
    assert b'Please enter a URL' in response.data


def test_invalid_url_rejected(client):
    response = client.post('/', data={
        'original_url': 'not a valid url'
    })
    assert response.status_code == 200
    assert b'Please enter a valid URL' in response.data


def test_custom_alias_created(client):
    response = client.post('/', data={
        'original_url': 'https://example.com',
        'custom_alias': 'testalias'
    })
    assert response.status_code == 302
    assert b'/result/testalias' in response.data or \
        response.headers['Location'].endswith('/result/testalias')
