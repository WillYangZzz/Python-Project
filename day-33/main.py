import requests
from datetime import datetime
import time

MY_LA = -36.848461
MY_LN = 174.763336

def is_iss_overhead():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LA - 5 <= iss_latitude <= MY_LA + 5 and MY_LN - 5 <= iss_longitude <= MY_LN + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LA,
        "lng": MY_LN,
        "formatted":0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset =int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
While True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection =



