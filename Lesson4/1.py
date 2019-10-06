import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.cbr.ru/scripts/XML_daily.asp"

response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")
def get_course(name):
    name = soup.find_all('valute', {'id': id})
    vals = soup.find({'charcode': name})
    return vals



print(get_course('azn'))
#result = float(get_course("R01235"))
#number = int(input("Сколько баксов нужно?: "))
#print(f"Чтобы купить {number} доллара(ов) нужно {number * result} деревянных.")

