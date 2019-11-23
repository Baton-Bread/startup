import requests
 
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
key = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97'
text = 'Hello'
lang = 'en-ru'
r = requests.post(url, data={'key': key, 'text': text, 'lang': lang}).json()
print(r["text"])


            elif message == "погода":
                url_1 = 'https://yandex.ru/pogoda/novosibirsk'
                response = requests.get(url_1)
                html = BeautifulSoup(response.content, 'lxml')
                grade = temp(html)
                stat = status(html)
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="В новосибирске " + grade + " градусов")
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="На улице: " + stat)