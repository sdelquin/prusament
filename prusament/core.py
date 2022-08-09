import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

import settings


def get_filaments():
    filaments = {}
    response = requests.get(settings.URL, headers={'User-Agent': generate_user_agent()})
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.select(settings.FILAMENT_CSS_PATH):
        filaments[a.text] = a['href']
    return filaments
