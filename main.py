from bs4 import BeautifulSoup
import requests

url = 'https://koronastop.lrv.lt/'
page = BeautifulSoup(requests.get(url).content, 'html.parser')
print(page)