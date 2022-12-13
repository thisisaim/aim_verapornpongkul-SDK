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
class Book:
    id: str = ""
    name: str = ""
    chapters: list = field(default_factory=list)


    def get_all_books(params={}):
        try:
            response = requests.get(BASEURL+"/book", headers=HEADERS, params=params)
            books_dictionary = response.json()
            total_books = books_dictionary["total"]
            books = []
            logging.info(f"Accessed {BASEURL}/book with status {response.status_code}")
            string_data = json.loads(response.text)

            for i in range(total_books):
                book = Book(books_dictionary["docs"][i]['_id'], 
                                            books_dictionary["docs"][i]['name'])
                books.append(book)
            return books
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")


    def get_book_by_id(id):
        try:
            response = requests.get(BASEURL+"/book/"+id, headers=HEADERS)
            logging.info(f"Accessed {BASEURL}/book/{id} with status {response.status_code}")
            string_data = json.loads(response.text)
            return json.dumps(string_data, indent=4)
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")


    def get_book_chapter_by_id(id):
        try:
            response = requests.get(BASEURL+"/book/"+id+"/chapter",
                headers=HEADERS)
            logging.info(f"Accessed {BASEURL}/book/{id}/chapter with status {response.status_code}")
            data = json.loads(response.text)
            return json.dumps(data, indent=4)
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")


