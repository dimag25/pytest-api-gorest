from Consts import TOKEN
import pytest
import requests
# fixture method - initialize request with headers


@pytest.fixture(scope='module')
def req():
    with requests.Session() as s:
        s.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}',
        })

        yield s
