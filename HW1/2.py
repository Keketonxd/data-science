# NASA API
# https://api.nasa.gov/planetary/apod?api_key=Ewlx0OB0OtleCH4kfaeMqQZWeJcfa1H81UcjHxWJ
import requests
from pprint import pprint

print('Получите количество пролетающих ближе всего к Земле.')

start_date = input(
    'Введите дату начала поиска астероидов в формате YYYY-MM-DD: ')
end_date = input(
    'Введите дату конца поиска астероидов в формате YYYY-MM-DD, значение по умолчанию - неделя с даты начала: ')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36"}
params = {'start-date': f"{start_date}",
          'end-date': f"{end_date}",
          "api_key": "Ewlx0OB0OtleCH4kfaeMqQZWeJcfa1H81UcjHxWJ"}
url = 'https://api.nasa.gov/neo/rest/v1/feed'

response = requests.get(url, params=params, headers=headers)

with open('HW1/2.json', 'w') as f:
    f.write(response.text)

data = response.json()
print(
    f"С {start_date} до {end_date} максимально близко по своим траекториям к Земле пролетело {data['element_count']} метеоритов.")
