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
class Chapter:
    id: str = ""
    chapterName: str = ""
    book: str = ""

    def get_all_chapters(params={}):
        try:
            response = requests.get(BASEURL+"/chapter", headers=HEADERS, params=params)
            logging.info(f"Accessed {BASEURL}/chapter with status {response.status_code}")
            data = response.json()
            chapters = []
            for i in data["docs"]:
                chapters.append(Chapter(
                i.get("_id"),
                i.get("chapterName"),
                i.get('book')
            ))
            #Check if > 1000 
            r = data["pages"] + 1
            for j in range(2, r):
                response_2 = requests.get(BASEURL+"/chapter", headers=HEADERS, params= params |{"page": i})
                try:
                    logging.info(f"Status {response_2.status_code}. Successfully accessed {BASEURL} page {i}.")
                    json_2 = response_2.json()["docs"]
                    for j in json_2:
                        chapters.append(Chapter(
                            j.get("_id"),
                            j.get("chapterName"),
                            j.get('book')
                        ))
                except RequestException as e2:
                    logging.error("An error occurred while making the request:", e2)
            return chapters
        except RequestException as e:
            logging.error("An error occurred while making the request:", e)


    def get_chapter_by_id(id):
        try:
            response = requests.get(BASEURL+"/chapter/"+id, 
                        headers=HEADERS)
            logging.info(f"Accessed {BASEURL}/chapter/{id} with status {response.status_code}")
            data = json.loads(response.text)
            return json.dumps(data, indent=4)
        except RequestException as e:
            logging.error("An error occurred while making the request:", e)