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

        if not req.json().get('success'):            
            error = req.json().get('error', {})
            error_code = error.get('code', {})

            if error_code == 101:
                raise Exception('unauthorized: User did not supply invalid access key')
            if error_code == 404:
                raise Exception('404_not_found: user requested resource does not exist')
            if error_code == 615:
                raise Exception('request_failed: API request failed')
        
        return req.json()

