from urllib import parse
import requests
import os
from dotenv import load_dotenv

load_dotenv()
ANIMALS_API_KEY= os.getenv("ANIMALS_API_KEY")
ANIMALS_API_URL="https://api.api-ninjas.com/v1/animals?"

def get_animals(searched_animal):
    """uses Ninja api to fetch animal's data documentation of the api
    can be found in the following link https://api-ninjas.com/api/animals"""
    data = {
        "name": searched_animal
    }
    encoded_data = parse.urlencode(data)
    response = requests.get(
        ANIMALS_API_URL+encoded_data,
        headers={'X-Api-Key': ANIMALS_API_KEY},
        timeout=5
    )
    return response.json()
