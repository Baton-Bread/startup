import requests
import bs4

def genres():

    html = "http://everynoise.com"
    response = requests.get(html)
 
    soup = bs4.BeautifulSoup(response.content, "lxml")
    genre = soup.find_all("div", {"class": "genre scanme"})
    for x in genre:
        g = print(x.text)
        if x.genre_scanme == "dark psytrance":
            pass

genres()