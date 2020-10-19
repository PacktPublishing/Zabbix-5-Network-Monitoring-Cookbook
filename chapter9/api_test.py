import requests
import json
from lxml import etree
import login

#User variables
url = login.address()
headers = {'Content-Type': 'application/json'}

parser = etree.XMLParser(remove_blank_text=True)


def main():
    token = login.login()
    host_dict = hostid_get(token)
    get_configuration(host_dict,token)
    login.logout(token)
