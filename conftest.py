from Utils.Consts import TOKEN
import pytest
import requests
import allure


# fixture method - initialize request with headers
@pytest.fixture(scope='module')
def req():
    with requests.Session() as s:
        s.headers.update({
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}',
        })

        yield s


@allure.title("Test GET HTTP Request")
def get_request(url, req):
    response = req.get(url)
    assert response.status_code == 200
    allure.attach(
        f"Request URL: {url}\nResponse Status Code: {response.status_code}\nResponse Content: {response.content}",
        name="HTTP GET Request Details",
        attachment_type=allure.attachment_type.JSON)
    return response


@allure.title("Test POST HTTP Request")
def post_request(url, data, req):
    response = req.post(url,data=data)
    assert response.status_code == 201, f"Expected Status [201], actual Status: {response.status_code}"
    allure.attach(
        f"Request URL: {url}\nRequest Body:{data}\nResponse Status Code: {response.status_code}"
        f"\nResponse Content: {response.content}",
        name="HTTP POST Request Details",
        attachment_type=allure.attachment_type.JSON)
    return response


@allure.title("Test POST HTTP Request")
def put_request(url, data, req):
    response = req.put(url, data=data)
    assert response.status_code == 200, f"Expected Status [200], actual Status: {response.status_code}"
    allure.attach(
        f"Request URL: {url}\nRequest Body:{data}\nResponse Status Code: {response.status_code}"
        f"\nResponse Content: {response.content}",
        name="HTTP PUT Request Details",
        attachment_type=allure.attachment_type.JSON)
    return response