from os import name
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36",
           "Accept": "application/vnd.github.v3+json"}
user = 'Keketonxd'
url = f'https://api.github.com/users/{user}/repos'
response = requests.get(url, headers=headers)
data = response.json()

with open('HW1/1.json', 'w') as f:
    f.write(response.text)

print(f'Репозитории пользователя {user}:')
for obj in data:
    print(obj['name'])
