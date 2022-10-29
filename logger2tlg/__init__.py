import requests


__author__ = 'Bauyrzhan Ospan'
__email__ = 'main@cleverest.tech'
__copyright__ = 'Copyright (c) 2022-2027 Bauyrzhan Ospan'
__license__ = 'MIT'
__version__ = '0.0.1'
__url__ = 'https://github.com/bauyrzhanospan/cleverest_debugger'


class Logger2tlg():
        def __init__(self, chat_id, bot_id) -> None:
            self.chat_id = chat_id
            self.bot_id = bot_id

        def log(self, text):
            try:
                requests.post(
                    url='https://api.telegram.org/bot{0}/{1}'.format(self.bot_id, "sendMessage"),
                    data={'chat_id': self.chat_id, 'text': text}
                ).json()
            except Exception as e:
                print("Error: " + str(e))

