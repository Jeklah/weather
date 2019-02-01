import click
import requests

DEFAULT_API_KEY = 'ac584b0c85fc034f3673c7ec1443cc36'


def current_weather(location, api_key):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    query_params = {
        'q': location,
        'appid': api_key or DEFAULT_API_KEY,
    }
    response = requests.get(url, params=query_params)
    return (response.json()['weather'][0]['description'],
            response.json()['wind']['speed'])


@click.command()
@click.argument('location')
@click.option('--wind', '-w', help="Wind information", is_flag=True)
@click.option('--api_key', '-a', help="Your api key for OpenWeatherMap")
def main(location, api_key, wind):
    """
    A little weather tool that shows you the current weather in a LOCATION of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:

    1. London,UK

    2. Canmore

    """
    weather, windWeather = current_weather(location, api_key)
    print "The weather in", location, "right now: ", weather, "."
    if wind:
        print "The wind speed in", location, "is:", windWeather, "."


if __name__ == "__main__":
    main()
