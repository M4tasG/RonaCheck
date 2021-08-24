from bs4 import BeautifulSoup
import requests
url = 'https://koronastop.lrv.lt/'
page = BeautifulSoup(requests.get(url).content, 'html.parser')
stats = page.find('div', class_='stats_list').find_all('div', class_='stats_item')

def get_ronastats():
    stats_arr = []
    for stat in stats:
        title = stat.find('div', class_='title')
        value = stat.find('div', class_='value')
        stats_arr.append(f'{title.text}: {value.text.strip()}')
    return stats_arr

def parse_value(index):
    return int(stats[index].find('div', class_="value").text.strip())

def get_ronacases():
    return parse_value(0)

def get_ronadeaths():
    return parse_value(1)

def get_ronapositive():
    return float(stats[3].find('div', class_="value").text.strip().replace(',','.')[:-1])

def get_ronavaccinated():
    return parse_value(4)

