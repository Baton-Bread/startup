import requests
from bs4 import BeautifulSoup

url = "https://news.mail.ru"

response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")



def get_news():
    response = ""
    news = soup.find_all("a", {"class": "list__text"})
    for el in news:
        if "http" in el['href']:
            href = el['href']
        else:
            href = url + el['href']
        response += f"{el.text}\nИсточник:{href}\n\n"

    return response

