import os
import json
import requests 
import yaml
import logging
from dataclasses import dataclass
logging.basicConfig(filename='sdk.log', level=logging.INFO)

from requests import RequestException

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(CURRENT_DIR, "config.yml"), "r") as ymlfile:
    config = yaml.safe_load(ymlfile)
    BASEURL = config['external']['base_url']
    HEADERS = {"Authorization": "Bearer " + config['external']['api_key']}

@dataclass()
class Character:
    id: str = ""
    height: str = ""
    race: str = ""
    gender: str = ""
    birth: str = ""
    spouse: str = ""
    death: str = ""
    realm: str = ""
    hair: str = ""
    name: str = ""
    wikiUrl: str = ""


    def get_character_by_id(id):
        try:
            response = requests.get(BASEURL+"/character/"+id, headers=HEADERS)
            logging.info(f"Accessed {BASEURL}/character/{id} with status {response.status_code}")
            data = json.loads(response.text)
            data = json.loads(response.text)
            return json.dumps(data, indent=4)
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")


    def get_character_quote_by_id(id):
        try:
            response = requests.get(BASEURL+"/character/"+id+"/quote", 
                headers=HEADERS)
            logging.info(f"Accessed {BASEURL}/character/{id}/quote with status {response.status_code}")
            data = json.loads(response.text)
            return json.dumps(data, indent=4)
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")


    def get_all_characters(params={}):
        try:
            response = requests.get(BASEURL+"/character", headers=HEADERS)
            logging.info(f"Accessed {BASEURL}/character with status {response.status_code}")
            data = response.json()
            characters = []
            for x in data["docs"]:
                characters.append(Character(
                    x.get("_id"),
                    x.get("height"),
                    x.get("race"),
                    x.get("gender"),
                    x.get("birth"),
                    x.get("spouse"),
                    x.get("death"),
                    x.get("realm"),
                    x.get("hair"),
                    x.get("name"),
                    
                ))
            r = data["pages"] + 1

            for i in range(2, r):
                try:
                    response_2 = requests.get(BASEURL+"/character",params= params |{"page": i}, headers=HEADERS)
                    data_2 = response.json()
                    for x in response_2['docs']:
                        characters.append(Character(
                        x.get("_id"),
                        x.get("height"),
                        x.get("race"),
                        x.get("gender"),
                        x.get("birth"),
                        x.get("spouse"),
                        x.get("death"),
                        x.get("realm"),
                        x.get("hair"),
                        x.get("name"),
                            ))
                except RequestException as e2:
                    logging.error(f"An error occurred while making the request: {e2}")
            data = json.loads(response.text)
            return characters
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")