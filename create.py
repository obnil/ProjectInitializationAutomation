import sys
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

token = os.getenv("TOKEN")
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'token ' + token,
    'Accept': 'application/vnd.github.v3+json'}


def create():
    repository = str(sys.argv[1])
    url = 'https://api.github.com/user/repos'
    data = {
        "name": repository,
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    if(response.status_code == 201):
        print("[✓] Succesfully created repository {}".format(repository))
        exit()
    else:
        print("[!] Failed created repository {}".format(repository))
        print('------------------------------')
        exit(response.text)

if __name__ == "__main__":
    create()
