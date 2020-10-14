import requests
import json


url = 'http://10.16.16.152/zabbix/api_jsonrpc.php?'
username = "API"
password = "password"

headers = {'Content-Type': 'application/json'}


def address():
    return url

def login():
    token = "null"

    #Login payload
    payload = {}
    payload['jsonrpc'] = '2.0'
    payload['method'] = 'user.login'
    payload['params'] = {}
    payload['params']['user'] = username
    payload['params']['password'] = password
    payload['id'] = 1

    #Logging in
    request = requests.post(url, data=json.dumps(payload), headers=headers)
    #Converting string to json
    data = request.json()
    json_string = json.dumps(data)

    #Filtering on the token only to use later on
    token = data["result"]
    return token



def logout(token):
    #Logout payload
    payload = {}
    payload['jsonrpc'] = '2.0'
    payload['method'] = 'user.login'
    payload['params'] = {}
    payload['params']['user'] = username
    payload['params']['password'] = password
    payload['auth'] = token
    payload['id'] = 1

    #Logging out
    request = requests.post(url, data=json.dumps(payload), headers=headers)
