import json
import random
import allure
from Utils.api import api
from Utils.Consts import USERS_ENDPOINT
from Utils.helpers import generate_user_data
from conftest import get_request, post_request, put_request
users_api = api(endpoint=USERS_ENDPOINT)


# Add user then get the user to see of all the details are correct
@allure.story("Create user test")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user(req):
    user_data = generate_user_data()
    res = post_request(url=users_api.api_endpoint, data=user_data, req=req)
    # check user data correct in get user api by id
    created_user = get_request(
        f'{users_api.api_endpoint}/{res.json()["id"]}', req)
    assert created_user.json()['name'] == json.loads(user_data)['name']
    assert created_user.json()['email'] == json.loads(user_data)['email']
    assert created_user.json()['gender'] == "male"
    assert created_user.json()['status'] == "active"


# Update your user and change the name, then get and see if all the details are correct
def test_update_user_name(req):
    user = get_request(url=users_api.api_endpoint, req=req).json().pop()
    original_username = user['name']
    print("\n original_username: ", original_username)
    user_data = generate_user_data()
    print("\n new user data: ", user_data)
    put_request(url=f'{users_api.api_endpoint}/{user["id"]}', data=user_data, req=req)
    assert get_request(url=f'{users_api.api_endpoint}/{user["id"]}', req=req).json()[
        'name'] == json.loads(user_data)["name"]


# Select 10 random distinct users and print their names
def test_10_random_distinct_users(req):
    users = get_request(url=users_api.api_endpoint, req=req).json()
    user_names = [user['name'] for user in users]
    random_users = random.sample(user_names, 10)
    for user in random_users:
        print(user)


# Iterate the users and print how many unique names there are, and how many users have
# the same name, sorted from the biggest to smallest.
def test_unique_names_counts(req):
    users = get_request(url=users_api.api_endpoint, req=req).json()
    user_names = [user['name'] for user in users]
    name_counts = {}
    for name in user_names:
        name_counts[name] = name_counts.get(name, 0) + 1
    # Printing number of unique names
    print("\nTotal unique names:", len(name_counts))
    # Sorting names based on frequency of occurrence
    sorted_names = sorted(name_counts.items(),
                          key=lambda x: x[1], reverse=True)
    # Printing sorted names and their occurrences
    print("\nUsers sorted by frequency of occurrence:")
    for name, count in sorted_names:
        print(f"{name}: {count} users")
