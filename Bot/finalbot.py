import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from modules.course import get_course
from modules.news import get_news
import requests
import json
from modules.weather import temp
from modules.weather import status
from bs4 import BeautifulSoup


def main():
    TOKEN = "55bd7986c04195010a138b05fdebb0c5802c0a9ef3f3cf4c5c6b7737612dc01964b9a203b41ba24fbba89"

    vk_session = vk_api.VkApi(token=TOKEN)



    vk = vk_session.get_api()

    hello = ["Привет!", "Категорически приветствую", "Рада тебя видеть! :3", "Чем могу помочь?"]

    how_are_you = ["Какие же дела у меня могут быть, если я бот?", "Да вот, помогаю 'человекам', таким как ты :)"]

    skills = "Список моих комманд\nкурс - выводит курс доллара и евро\nновости - выведу тебе актуальный список новостей\nпереводчик - переведу тебе все что ты мне напишешь. Чтобы выйти из переводчика введи 'выход'\nпогода - выведу погоду, пока что, только в новосибирске"


    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            message = event.message.lower()
            if message == "курс":
                response = f"""
                За 1 доллар дают {get_course("R01235")} деревянных.
                """
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=response)
            elif message == "покекать":
                memes = ["photo-147286578_457450491", "photo-147286578_457450484", "photo-147286578_457450483"]
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), attachment=random.choice(memes))
            elif message == "новости":
                response = get_news()
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=response)
            elif message == "привет":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=random.choice(hello))
            elif message == "как дела":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=random.choice(how_are_you))
            elif message == "комманды" or message == "что ты умеешь":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=skills)
            elif message == "переводчик":
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="Я в режиме переводчика. Вводи все, что нужно перевести на русский.")
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                        message = event.message.lower()

                        

                        if message == "выход":
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="Режим 'Англичанина' выключен")
                            main()

                        

                        typing = event.text
                        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
                        key = 'trnsl.1.1.20191123T081608Z.8ec51c73a4267699.76671010e98e75c6e422a9e9b3ac595b3b6b657d' 
                        lang = 'ru-en','en-ru' 
                        r = requests.post(url, data={'key': key, 'text': typing, 'lang': lang}) 
                        good_text = json.loads(r.text)['text'][0]


                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=good_text)

            elif message == "погода":
                url_1 = 'https://yandex.ru/pogoda/novosibirsk'
                response = requests.get(url_1)
                html = BeautifulSoup(response.content, 'lxml')
                grade = temp(html)
                stat = status(html)
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="В новосибирске " + grade + " градусов")
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="На улице: " + stat)            



            else:
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="Пока что не понимаю тебя :(")
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="Чтобы посмотреть список моих возможностей введи 'комманды'")




main()

