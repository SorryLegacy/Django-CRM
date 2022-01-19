import requests
from .models import TeleSettings


def send_telegram(name, phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_text)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            first_right = text.find('{')
            first_left = text.find('}')
            last_right = text.rfind('{')
            last_left = text.rfind('}')

            part_1 = text[0:first_right]
            part_2 = text[first_left + 1:last_right]
            part_3 = text[last_left:-1]

            text_slice = part_1 + name + part_2 + phone + part_3
        else:
            text_slice = text

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice,

            })

        except:
            pass

        finally:
            if req.status_code != 200:
                print("Ошибка отправки")
            elif req.status_code == 500:
                print("Ошибка 500")
            else:
                print("Всё окей")


    else:
        pass
