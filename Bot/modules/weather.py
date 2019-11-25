import requests #Активировать библиотеку requests
from bs4 import BeautifulSoup #Подключить инструмент из библиотеки

def temp(html):
    return html.find('span', {'class': 'temp__value'}).text 
def status(html):
    return html.find('div', {'class': 'link__condition day-anchor i-bem'}).text
def sunrise(html):
    return html.find('dd', {'class': 'sunrise-sunset__value'}).text
def sunset(html):
    return html.find('dd', {'class': 'sunrise-sunset__value'}).text





