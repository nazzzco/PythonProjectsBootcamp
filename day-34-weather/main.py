import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = "856335270a6e796c4ef2614d09db94a3"
MY_LAT = 42.697708
MY_LONG = 23.321867
TWILIO_CODE = "TMK2GKMLAHFL5DKYZFNT1A87"
account_sid = 'ACec8cfb89db9c6532bc11460d1f536bd8'
auth_token = '59bf71b830c90c1189e72008daa33355'

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4,
}

response =requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
print(data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
               .create(
            body="Днес ще вали. Вземи ☂️! Целуни Иветка ️❤️️❤️️❤️",
            from_="+15103690061",
            to="+359884082247",
    )

    print(message.sid)