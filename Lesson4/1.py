import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.cbr.ru/scripts/XML_daily.asp"


response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
def get_course(chr_code, count):
    valutes = soup.find_all("valute")
    for x in valutes:
        if x.charcode.text == chr_code:
            nominal = int(x.nominal.text)
            value = float(x.value.text.replace(",", "."))
            print(f"За {nominal*count} {chr_code} дают {nominal * value * count} дере")

def calc():
