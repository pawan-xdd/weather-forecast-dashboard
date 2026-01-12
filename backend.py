import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API = os.getenv("API_KEY")


def get_data(place,forecast_days):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={WEATHER_API}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Bhilai", forecast_days=6))