import os
import requests
from twilio.rest import Client

account_sid = os.environ.get('account_sid')
auth_token = "8bb6dc5db6682418700cf56715c47c09"
client = Client(account_sid, auth_token)

weather_values = []
weather = []

api_key = os.environ.get("API_KEY")
print(api_key)

parameters = {
    "lat": 19.4285,
    "lon": -99.1277,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
api_call = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

print("The status code is:", api_call.status_code)
api_call = api_call.json().values()

for values in api_call:
    weather_values.append(values)
whether_values = weather_values[4:]

for i in range(0, 12):
    weather.append(whether_values[0][i])

for i in range(0, 12):
    if weather[i]["weather"][0]["id"] < 700:
        print("Bring an umbrella")
        message = client.messages \
            .create(
                 body="The forecast is a rainy day. Bring an Umbrella!☔️",
                 from_='+14154170291',
                 to='+525522494955'
            )
        break
