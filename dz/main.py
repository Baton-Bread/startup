import requests
import bs4
 
response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")
 
soup = bs4.BeautifulSoup(response.content, "lxml")
 
chr_code = "CNY"
count = 10
 
valutes = soup.find_all("valute")
 
for x in valutes:
    if x.charcode.text == chr_code:
        nominal = int(x.nominal.text)
        value = float(x.value.text.replace(",", "."))
        print(f"За {nominal*count} {chr_code} дают {nominal * value * count}руб")