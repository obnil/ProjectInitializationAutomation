import sys
import os
from dotenv import load_dotenv
import requests

load_dotenv()

username = os.getenv("USERNAME")
token = os.getenv("TOKEN")

def delete():
    repository = str(sys.argv[1])
    url = 'https://api.github.com/repos/' + username + '/' + repository
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'token ' + token,
        'Accept': 'application/vnd.github.v3+json'}
    response = requests.delete(url=url, headers=headers)
    if(response.status_code == 204):
        print('[✓] Delete {} success'.format(repository))
    else:
        print('[!] Delete {} failed'.format(repository))
        print('------------------------------')
        print(response.text)
        print('------------------------------')


if __name__ == "__main__":
    delete()
