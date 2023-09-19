import os
import requests
from datetime import datetime

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
AUTH_TOKEN = os.environ['SHEETY_AUTH_TOKEN']
GENDER = os.environ['GENDER']
WEIGHT_KG = os.environ['WEIGHT_KG']
HEIGHT_CM = os.environ['HEIGHT_CM']
AGE = os.environ['AGE']
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']

user_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

body = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, headers=headers, json=body)
results = response.json()

today = datetime.now()

for exercise in results["exercises"]:
    params = {'workout': {
        "date": today.date().strftime("%d/%m/%Y"),
        "time": today.time().strftime("%H:%M:%S"),
        "exercise": exercise['name'].title(),
        "duration": round(exercise['duration_min']),
        "calories": round(exercise['nf_calories']),

    }}

    sheety_headers = {
        "Authorization": AUTH_TOKEN,
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=params, headers=sheety_headers)
    print(response.text)
