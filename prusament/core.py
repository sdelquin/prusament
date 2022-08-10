import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from logzero import logger
from user_agent import generate_user_agent

import settings


class Handler:
    def __init__(self, store: Path = settings.FILAMENTS_DAT) -> None:
        self.store = store
        self.filaments = {}

    def get_filaments_from_tinermaq(self, force_request: bool = False) -> dict:
        logger.info('Getting available filaments from tinermaq website')
        if self.filaments and not force_request:
            return self.filaments
        self.filaments = {}
        response = requests.get(settings.URL, headers={'User-Agent': generate_user_agent()})
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.select(settings.FILAMENT_CSS_PATH):
            self.filaments[a.text] = a['href']
        return self.filaments

    def save_filaments_to_store(self) -> None:
        logger.info(f'Saving filaments to {self.store}')
        with open(self.store, 'w') as f:
            csvwriter = csv.writer(f)
            for item in self.filaments.items():
                csvwriter.writerow(item)

    def load_filaments_from_store(self) -> dict:
        logger.info(f'Loading filaments from {self.store}')
        filaments = {}
        try:
            with open(self.store) as f:
                csvreader = csv.reader(f)
                for filament, url in csvreader:
                    filaments[filament] = url
        except FileNotFoundError:
            logger.warning(f'File {self.store} not found')
        return filaments

    def get_filament_updates(self) -> tuple[dict, dict]:
        logger.info('Getting filament updates from tinermaq website')
        tinermaq_filaments = self.get_filaments_from_tinermaq()
        stored_filaments = self.load_filaments_from_store()

        logger.debug('Checking added filaments')
        added_filaments = {}
        for filament, url in tinermaq_filaments.items():
            if filament not in stored_filaments:
                added_filaments[filament] = url

        logger.debug('Checking removed filaments')
        removed_filaments = {}
        for filament, url in stored_filaments.items():
            if filament not in tinermaq_filaments:
                removed_filaments[filament] = url

        return added_filaments, removed_filaments
