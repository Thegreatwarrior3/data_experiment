import os
from dotenv import load_dotenv

import requests

load_dotenv()

access_key = os.getenv('ACCESS_KEY')


class WEATHERSTACK(object):
    def __init__(self):
        self.host = 'http://api.weatherstack.com/current'        
        self.requests = requests.Session()

    def current_weather(self, city):
        params = {
            'access_key': access_key,
            'query': city
        }

        req = self.requests.get(self.host, params=params)

        return req

