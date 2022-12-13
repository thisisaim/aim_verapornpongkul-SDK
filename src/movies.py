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
class Movie:
    id: str = ""
    name: str = ""
    run_time_minutes: int = 0
    budget_millions: int = 0
    box_office_revenue_millions: int = 0
    academy_award_nominations: int = 0
    academy_award_wins: int = 0
    rotten_tomatoes_score: float = 0

    def get_all_movies(params={}):
        try:
            response = requests.get(BASEURL+"/movie", headers=HEADERS, params=params)
            logging.info(f"Accessed {BASEURL}/movie with status {response.status_code}")
            data = response.json()
            number_of_movies = num_of_movies = data["total"] if data["total"] < data["limit"] else data["limit"]
            movies = []
            for i in range(num_of_movies):
                movies.append(Movie(
                data["docs"][i]["_id"],
                data["docs"][i]["name"],
                data["docs"][i]["runtimeInMinutes"],
                data["docs"][i]["budgetInMillions"],
                data["docs"][i]["boxOfficeRevenueInMillions"],
                data["docs"][i]["academyAwardNominations"],
                data["docs"][i]["academyAwardWins"],
                data["docs"][i]["rottenTomatoesScore"],
            ))
            return movies
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")


    def get_movie_by_id(id):
        try:
            response = requests.get(BASEURL+"/movie/"+id, headers=HEADERS)
            logging.info(f"Accessed {BASEURL}/movie/{id} with status {response.status_code}")
            data = json.loads(response.text)
            return json.dumps(data, indent=4)
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")


    def get_movie_quote_by_id(id):
        try:
            response = requests.get(BASEURL+"/movie/"+id+"/quote", 
                headers=HEADERS)
            logging.info(f"Accessed {BASEURL}/movie/{id}/quote with status {response.status_code}")
            data = json.loads(response.text)
            return json.dumps(data, indent=4)
        except RequestException as e:
            logging.error(f"An error occurred while making the request: {e}")
