import json
import random
import uuid

import pytest
import requests
from api import api
from Consts import USERS_ENDPOINT

users_api = api(endpoint=USERS_ENDPOINT)


# fixture method - initialize request with headers
@pytest.fixture(scope='module')
def users_req():
    with requests.Session() as s:
        s.headers.update({
            'Content-Type': 'application/json',
            'Authorization': users_api.authorization,
        })

        yield s


def generate_user_data():
    unique_name = f"DimaGurevich_{uuid.uuid4()}"
    unique_email = f"gurevich@{uuid.uuid4()}"
    return '{"name":"%s", "gender":"male", "email":"%s", ' \
           '"status":"active"} ' % (unique_name, unique_email)


# Add user then get the user to see of all the details are correct
def test_create_user(users_req):
    user_data = generate_user_data()
    res = users_req.post(url=users_api.api_endpoint, data=user_data)
    assert res.status_code == 201, f"Expected Status [201], actual Status: {res.status_code}"
    # check user data correct in get user api by id
    created_user = users_req.get(f'{USERS_ENDPOINT}/{res.json()["id"]}')
    assert created_user.json()['name'] == json.loads(user_data)['name']
    assert created_user.json()['email'] == json.loads(user_data)['email']
    assert created_user.json()['gender'] == "male"
    assert created_user.json()['status'] == "active"


# Update your user and change the name, then get and see if all the details are correct
def test_update_user_name(users_req):
    user = users_req.get(url=users_api.api_endpoint).json().pop()
    original_username = user['name']
    print("\n original_username: ", original_username)
    user_data = generate_user_data()
    print("\n new user data: ", user_data)
    res = users_req.put(url=f'{USERS_ENDPOINT}/{user["id"]}', data=user_data)
    assert res.status_code == 200, f"Expected Status [200], actual Status: {res.status_code}"
    assert users_req.get(url=f'{USERS_ENDPOINT}/{user["id"]}').json()['name'] == json.loads(user_data)["name"]


# Select 10 random distinct users and print their names
def test_10_random_distinct_users(users_req):
    users = users_req.get(url=users_api.api_endpoint).json()
    user_names = [user['name'] for user in users]
    random_users = random.sample(user_names, 10)
    for user in random_users:
        print(user)


# Iterate the users and print how many unique names there are, and how many users have
# the same name, sorted from the biggest to smallest.
def test_unique_names_counts(users_req):
    users = users_req.get(url=users_api.api_endpoint).json()
    user_names = [user['name'] for user in users]
    name_counts = {}
    for name in user_names:
        name_counts[name] = name_counts.get(name, 0) + 1
    # Printing number of unique names
    print("\nTotal unique names:", len(name_counts))
    # Sorting names based on frequency of occurrence
    sorted_names = sorted(name_counts.items(), key=lambda x: x[1], reverse=True)
    # Printing sorted names and their occurrences
    print("\nUsers sorted by frequency of occurrence:")
    for name, count in sorted_names:
        print(f"{name}: {count} users")
