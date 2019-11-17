import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from modules.course import get_course
from modules.news import get_news


def main():
    TOKEN = "55bd7986c04195010a138b05fdebb0c5802c0a9ef3f3cf4c5c6b7737612dc01964b9a203b41ba24fbba89"

    vk_session = vk_api.VkApi(token=TOKEN)

    vk = vk_session.get_api()

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
            else:
                vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="Введи правильную комманду :3")                    

main()