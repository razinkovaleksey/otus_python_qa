import requests
import pytest


def test_create_resource():
    body = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body)
    assert response.json()['title'] == body['title']
    assert response.json()['body'] == body['body']
    assert response.json()['userId'] == body['userId']
    assert response.json()['id'] == 101


@pytest.mark.parametrize('param,value', (('title', 'spam'), ('body', 'eggs')))
def test_patch_resource(param, value):
    body_ = {param: value
             }
    response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', data=body_)
    assert response.json()[param] == value


@pytest.mark.parametrize('post_id', (1, 2, 3))
def test_update_resource(post_id):
    body = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.put('https://jsonplaceholder.typicode.com/posts/{post_id}'.format(post_id=post_id), json=body)
    assert response.json()['title'] == body['title']
    assert response.json()['body'] == body['body']
    assert response.json()['userId'] == body['userId']
    assert response.json()['id'] == post_id


def test_delete_resource():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    assert not response.json()


@pytest.mark.parametrize('user_id', (1, 2))
def test_assert_post_by_users(user_id):
    response = requests.get('https://jsonplaceholder.typicode.com/posts?userId={user_id}'.format(user_id=user_id))
    for post in response.json():
        assert post['userId'] == user_id
