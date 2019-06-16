import json
from datetime import date

import requests


class Fetcher:
    url = "http://api.nbp.pl/api/cenyzlota"
    data = b""

    def __init__(self, url):
        self.fetch_data(url)

    def fetch_data(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.data = request.content


class JSONParser:
    def __init__(self, json_data):
        self.set_data(self.parse(json_data))

    def parse(self, json_data):
        if json_data == b"":
            raise ValueError("Empty data")
        else:
            return json.loads(json_data)[0]
    
    def set_data(self, parsed_json):
        self.date = date.fromisoformat(parsed_json["data"])
        self.price = parsed_json["cena"]
