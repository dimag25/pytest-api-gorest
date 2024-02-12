import json
import random
import uuid

import pytest
import requests
from api import api
from Consts import POSTS_ENDPOINT, USERS_ENDPOINT

posts_api = api(endpoint=POSTS_ENDPOINT)
users_api = api(endpoint=USERS_ENDPOINT)


# fixture method - initialize request with headers
@pytest.fixture(scope='module')
def req():
    with requests.Session() as s:
        s.headers.update({
            'Content-Type': 'application/json',
            'Authorization': posts_api.authorization,
        })

        yield s


def generate_post_data(user_id, title, body):
    return '{"user_id": "%s", "title": "%s", "body": "%s"}' \
           % (user_id, title, body)


# Post 3 Posts in the following order
'''a. Post 1
b. Post 2
i. Comment 1
ii. Comment 2
c. Post 3
i. Comment 3'''


def test_post_diff_three_posts(req):
    user = req.get(url=users_api.api_endpoint).json()[0]
    create_post = req.post(url=f'{users_api.api_endpoint}/{user["id"]}/posts',
                           data=generate_post_data(user_id=user['id'], title='Post1', body='post1...'))
    assert create_post.status_code == 201


# Get all users posts and comment and print them in the following order:
#   Post 1
# ... (comments)
# Post2
# ... (comments)
# etc...
def test_user_posts(req):
    user = req.get(url=users_api.api_endpoint).json()[0]
    user_posts = req.get(url=f'{users_api.api_endpoint}/{user["id"]}/posts')
    for post in user_posts.json():
        print(f'\n{post["title"]}')
        post_comments = req.get(url=f'{users_api.api_endpoint}/{post["id"]}/comments')
        if post_comments.status_code != 404:
            print(post_comments)
