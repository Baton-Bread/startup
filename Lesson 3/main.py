import requests #Активировать библиотеку requests
from bs4 import BeautifulSoup #Подключить инструмент из библиотеки

def temp(html):
    return html.find('span', {'class': 'temp__value'}).text #"Отдать" информацию о температуре
def status(html):
    return html.find('div', {'class': 'link__condition day-anchor i-bem'}).text
def sunrise(html):
    return html.find('dd', {'class': 'sunrise-sunset__value'}).text
def sunset(html):
    return html.find('dd', {'class': 'sunrise-sunset__value'}).text


url = 'https://yandex.ru/pogoda/novosibirsk'
response = requests.get(url)
html = BeautifulSoup(response.content, 'lxml')
print("Сегодня в городе Новосибирск", temp(html))
print("На улице:", status(html))
print(sunset(html))
print(sunrise(html))

