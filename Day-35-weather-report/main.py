import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC4e9a75c82936be926e961e43f864fb11"
auth_token = "662fe556fa6a50245f899c24f3d297eb"

weather_params ={
    "lat": -36.848461,
    "lon": 174.763336,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weawther_slice = weather_data["hourly"][:12]
# hourly_data = weather_data["hourly"][0]["weather"][0]["id"]

will_rain = False
for hour_data in weawther_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+12083298249",
        to="+64221640190"
    )
    print(message.status)


