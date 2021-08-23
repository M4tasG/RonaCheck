from bs4 import BeautifulSoup
import requests

def get_ronastats():
    url = 'https://koronastop.lrv.lt/'
    page = BeautifulSoup(requests.get(url).content, 'html.parser')
    stats = page.find('div', class_='stats_list').find_all('div', class_='stats_item')
    stats_arr = []
    for stat in stats:
        title = stat.find('div', class_='title')
        value = stat.find('div', class_='value')
        #stats_arr += f'{title.text}: {value.text.strip()}'
        stats_arr.append(f'{title.text}: {value.text.strip()}')
    return stats_arr
