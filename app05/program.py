"""
App 05 - weather client to show local weather using requests and beautifulsoup4
to scrape wunderground.com
"""

from bs4 import BeautifulSoup
import requests
from collections import namedtuple

Weather = namedtuple('Weather', 'location, conditions, temp, units')

def get_zip():
    """
    Get the user's zipcode
    """
    zip = input('Enter your zipcode (e.g. 90210): ')
    return int(zip)


def get_page(zip):
    """
    Get the html response from wunderground.com for the user's zip code
    """
    url = "http://www.wunderground.com/weather/{}".format(zip)
    result = requests.get(url)
    if (result.status_code == 200):
        return result.content
    return "ERROR! Could not download HTML content"


def get_weather(content):
    """
    Parse the city/state location, temp/units and current conditions
    """
    soup = BeautifulSoup(content, 'html.parser')
    location = soup.find(class_='city-header').find('h1').get_text().strip()
    conditions = soup.find(class_='condition-icon').find('p').get_text().strip()
    temp = soup.find(class_='wu-value').get_text().strip()
    units = soup.find(class_='wu-label').get_text().strip()

    return Weather(location, conditions, temp, units)


def print_weather(weather):
    """
    Print the weather conditions
    """
    print("The current weather in {0} is {1} {2} and {3}".format(weather.location, weather.temp, weather.units, weather.conditions))


def main():
    zip = get_zip()
    content = get_page(zip)
    weather = get_weather(content)
    print_weather(weather)

if __name__ == '__main__':
    main()