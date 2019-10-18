import requests


def test_with_param(url):
    response = requests.get(url)
    assert response.status_code == 200
