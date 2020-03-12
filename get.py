import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

token = os.getenv("TOKEN")

def get():
    url = 'https://api.github.com/user/repos?sort=created'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'token ' + token,
        'Accept': 'application/vnd.github.v3+json'}
    response = requests.get(url=url, headers=headers)
    if(response.status_code == 200):
        print('[✓] Get repositorys success')
        repositoryList = json.loads(response.text)
        print('You have ['+ str(len(repositoryList)) +'] repositorys')
        for repository in repositoryList:
            print(repository['name'])
    else:
        print('[!] Get repositorys failed')
        print('------------------------------')
        print(response.text)
        print('------------------------------')

if __name__ == "__main__":
    get()
