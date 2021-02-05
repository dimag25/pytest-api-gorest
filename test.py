import pytest
import requests

from api import api

reqApi = api('admin', 'admin')


# fixture method - initialize request with headers
@pytest.fixture(scope='module')
def req():
    with requests.Session() as s:
        s.headers.update({
            'Accept': 'application/json',
            'Authorization': reqApi.authorization,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        })

        yield s


# send wrong password, userName=admin
def test_wrong_password(req):
    reqApi.setAuthorization('admin', 'a')
    req.headers['Authorization'] = reqApi.authorization
    res = req.get(reqApi.apiUrl.format(1), verify=False)
    assert res.status_code == 401, "Expected Status [401], actual Status: {0} " \
                                   "Connection Succeed with wrong password: {1} , userName: {2}".format(res.status_code,
                                                                                                        reqApi.password,
                                                                                                        reqApi.userName)


# send wrong userName, password=admin
def test_wrong_userName(req):
    reqApi.setAuthorization('aaa', 'admin')
    req.headers['Authorization'] = reqApi.authorization
    res = req.get(reqApi.apiUrl.format(1))
    assert res.status_code == 401, "Expected Status [401], actual Status: {0} " \
                                   "Connection Succeed with wrong password: {1} , userName: {2}".format(res.status_code,
                                                                                                        reqApi.password,
                                                                                                        reqApi.userName)


# check for "" in names of responses.
def test_emptyNames(req):
    for page in range(1, 100):
        resBody = req.get(reqApi.apiUrl.format(page)).json()
        for player in resBody:
            assert player['Name'] != "", "Empty Name Found for player id= {0} , page= {1}".format(player['ID'], page)


# check for duplicate player ids in diffrenet pages.
def test_duplicate_playersIds(req):
    totalPlayerDict = {}  # key: : player id, #value: tuple: player name ,page that player found
    for page in range(1, 100):
        resBody = req.get(reqApi.apiUrl.format(page)).json()
        for player in resBody:
            if totalPlayerDict.get(player["ID"]) is None:
                totalPlayerDict.setdefault(player["ID"], (player["Name"], page))
            else:  # if player id already exists - meaning duplicate player id appears.
                if player["Name"] == totalPlayerDict.get(player["ID"])[0]:  # player with same id , and same name.
                    raise ValueError('Duplicate Player found, ID :{0} ,Name:{1} ,Found on pages={2},{3} '
                                     .format(player["ID"], player["Name"], page, totalPlayerDict.get(player["ID"])[1]))


# if all names are nulls/empty in page
def test_emptyPage(req):
    for page in range(1, 100):
        pageDict = {}
        resBody = req.get(reqApi.apiUrl.format(page)).json()
        for player in resBody:
            pageDict[player['ID']] = player['Name']
        if all(value == 'null' or value == '' for value in pageDict.values()):
            raise ValueError('Page :{0} is without correct names, all names are null or empty'.format(page))


# Same page has different response – with empty names/without empty.
def test_diffResponseForSamePage(req):
    page = 1
    resBody1 = req.get(reqApi.apiUrl.format(page)).json()
    resBody2 = req.get(reqApi.apiUrl.format(page)).json()
    for player1, player2 in zip(resBody1, resBody2):
        if player1["ID"] == player2["ID"]:
            if player1["Name"] != player2["Name"]:
                raise ValueError(
                    'Page {0} have differenet responses , player Id :{1} first response Name :{2} , second response Name :{3} '
                        .format(page, player1["ID"], player1['Name'], player2['Name']))
