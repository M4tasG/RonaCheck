from bs4 import BeautifulSoup
import requests


url = 'https://koronastop.lrv.lt/'
page = BeautifulSoup(requests.get(url).content, 'html.parser')
stats = page.find('div', class_='stats_list').find_all('div', class_='stats_item')
for stat in stats:
    title = stat.find('div', class_='title')
    value = stat.find('div', class_='value')
    print(f'{title.text}: {value.text.strip()}')

