"""
INFO 465 - Day 1 starter script

This makes one request to the Open-Meteo weather API and prints part of
what comes back. You are not expected to understand every line yet --
real Python instruction starts in Week 3. For today, this just needs to
run, so there's something real to change, commit, and push.

Open-Meteo needs no API key and no signup, which is why we're using it
tonight instead of your project's real API.
"""

import requests

# Richmond, VA -- change these to your own hometown later and re-run.
LATITUDE = 37
LONGITUDE = -77


def get_current_weather(latitude, longitude):
    """Ask Open-Meteo for the current weather at a location."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    }
    response = requests.get(url, params=params)
    return response.json()


def main():
    data = get_current_weather(LATITUDE, LONGITUDE)
    current = data["current"]
    print("Current weather:")
    print(f"  Temperature: {current['temperature_2m']}°C")
    print(f"  Wind speed:  {current['wind_speed_10m']} km/h")


if __name__ == "__main__":
    main()
