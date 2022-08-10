from pathlib import Path
from typing import Iterable

import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

import settings


def get_filaments() -> dict:
    filaments = {}
    response = requests.get(settings.URL, headers={'User-Agent': generate_user_agent()})
    soup = BeautifulSoup(response.text, 'html.parser')
    for a in soup.select(settings.FILAMENT_CSS_PATH):
        filaments[a.text] = a['href']
    return filaments


def load_filaments(file: Path = settings.FILAMENTS_DAT) -> set:
    filaments = set()
    with open(file) as f:
        for filament in f:
            filaments.add(filament.strip())
    return filaments


def save_filaments(filaments: Iterable, file: Path = settings.FILAMENTS_DAT) -> None:
    with open(file, 'w') as f:
        for filament in filaments:
            f.write(f'{filament}\n')


def get_new_filaments() -> set:
    saved_filaments = load_filaments()
    current_filaments = set(get_filaments())
    return current_filaments - saved_filaments
