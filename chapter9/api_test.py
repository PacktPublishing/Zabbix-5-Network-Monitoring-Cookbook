import requests
import json

#Zabbix login
url = "http://10.16.16.152/zabbix/api_jsonrpc.php"
username = "API"
password = "password"


#Function to request API token
def get_api_token(url):

    payload = {
        "jsonrpc":"2.0",
        "method":"user.login",
        "params":{"user":username,"password":password},
        "id": 1,
        "auth": None
    }

    resp = requests.post(url=url, json=payload )
    out = resp.json()

    return out['result']

#Retrieve our host ID, hostname and interfaces of all our Zabbix hosts

def get_hosts(api_token, url):

    payload = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "interfaceid",
            "ip",
            "main"
        ]
    },
    "id": 2,
    "auth": api_token
    }

    resp = requests.post(url=url, json=payload )
    out = resp.json()


#API token request

api_token = (get_api_token(url))

zabbix_hosts = get_hosts(api_token,url)
generate_host_file(zabbix_hosts,"/home/results")
