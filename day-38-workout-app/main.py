import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 178
AGE = 34
APP_ID = "0c615a7e"
API_KEY = "6cf454ecc5d335f42b8a8fb14e62941a"

end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/38bb5310f5bfb3f4f199ffe15b77a3ec/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheety_headers = {
    "Authorization": "Bearer todayisSunday"
}

user_input = input("What exercises you've done?")

params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=end_point, json=params, headers=headers, verify=False)
data = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_headers, verify=False)

    print(sheet_response.text)