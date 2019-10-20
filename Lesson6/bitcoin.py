import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://alpari.com/ru/markets/crypto/bitcoin/"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')

def get_bitcoin():
    html = soup.find('div', {'class' : 'analytics-crypto-item__instrument-price-left'})
    return html.text.replace(",", ".")



