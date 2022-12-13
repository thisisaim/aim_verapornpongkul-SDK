import os
import json
import requests 
import yaml
import logging
from dataclasses import dataclass, field
logging.basicConfig(filename='sdk.log', level=logging.INFO)

from requests import RequestException

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(CURRENT_DIR, "config.yml"), "r") as ymlfile:
    config = yaml.safe_load(ymlfile)
    BASEURL = config['external']['base_url']
    HEADERS = {"Authorization": "Bearer " + config['external']['api_key']}

@dataclass
class Quote:
    id: str = ""
    dialog: str = ""
    movie: str = ""
    character: str = ""

    def get_all_quotes(params={}):
        try:
            response = requests.get(BASEURL+"/quote",params=params, headers=HEADERS)
            logging.info(f"Status {response.status_code}. Successfully accessed {BASEURL}.")
            data = response.json()
            quotes = []
            for x in data["docs"]:
                quotes.append(Quote(
                    x["id"],
                    x["dialog"],
                    x["movie"],
                    x["character"]
                ))
            r = 0 if  params.get("limit") else data["pages"]+1 
            for i in range(2,r):
                try:
                    response_2 = requests.get(BASEURL+"/quote",params= params |{"page": i}, headers=HEADERS)
                    logging.info(f"Status {response_2.status_code}. Successfully accessed {BASEURL}/quote page {i}.")
                    response_2 = response_2.json()
                    for x in response_2["docs"]:
                        quotes.append(Quote(
                            x["id"],
                            x["dialog"],
                            x["movie"],
                            x["character"]
                        ))
                except RequestException as e2:
                    logging.error(f"An error occurred while making the request: {e2}")
            return quotes
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")


    def get_movie_quote_by_id(id):
        try:
            response = requests.get(BASEURL+"/quote/"+id, headers=HEADERS)
            logging.info(f"Accessed {BASEURL}/quote/{id} with status {response.status_code}")
            data = json.loads(response.text)
            return json.dumps(data, indent=4)
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")
