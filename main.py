from bs4 import BeautifulSoup
import requests
from ronacheck import get_ronastats
from win10toast import ToastNotifier
"""
url = 'https://koronastop.lrv.lt/'
page = BeautifulSoup(requests.get(url).content, 'html.parser')
stats = page.find('div', class_='stats_list').find_all('div', class_='stats_item')
for stat in stats:
    title = stat.find('div', class_='title')
    value = stat.find('div', class_='value')
    print(f'{title.text}: {value.text.strip()}')
"""
stats = get_ronastats()

complete_string = f"""
{stats[0]}
{stats[1]}
"""

toast = ToastNotifier()
toast.show_toast("RonaCheck",complete_string,duration=10)