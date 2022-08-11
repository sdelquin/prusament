import csv
from pathlib import Path
from typing import Iterable

import requests
from bs4 import BeautifulSoup
from logzero import logger
from rich.console import Console
from rich.markdown import Markdown
from user_agent import generate_user_agent

import settings
from prusament.utils import init_sendgrid, render_message


class Filament:
    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self.url = url

    def __str__(self) -> str:
        return f'{self.name}: {self.url}'

    def __eq__(self, other: object) -> bool:
        return self.name == other.name

    def as_iterable(self) -> Iterable:
        return self.name, self.url

    def as_markdown(self):
        return f'[{self.name}]({self.url})'


class Handler:
    def __init__(self, store: Path = settings.FILAMENTS_DAT) -> None:
        self.store = store
        self.filaments = []

    def get_filaments_from_tinermaq(self, force_request: bool = False) -> dict:
        logger.info('Getting available filaments from tinermaq website')
        if self.filaments and not force_request:
            return self.filaments
        self.filaments = []
        response = requests.get(settings.URL, headers={'User-Agent': generate_user_agent()})
        soup = BeautifulSoup(response.text, 'html.parser')
        for a in soup.select(settings.FILAMENT_CSS_PATH):
            filament = Filament(a.text, a['href'])
            self.filaments.append(filament)
        return self.filaments

    def save_filaments_to_store(self) -> None:
        logger.info(f'Saving filaments to {self.store}')
        with open(self.store, 'w') as f:
            csvwriter = csv.writer(f)
            for filament in self.filaments:
                csvwriter.writerow(filament.as_iterable())

    def load_filaments_from_store(self) -> dict:
        logger.info(f'Loading filaments from {self.store}')
        filaments = []
        try:
            with open(self.store) as f:
                csvreader = csv.reader(f)
                for name, url in csvreader:
                    filament = Filament(name, url)
                    filaments.append(filament)
        except FileNotFoundError:
            logger.warning(f'File {self.store} not found')
        return filaments

    def get_filament_updates(self) -> tuple[dict, dict]:
        logger.info('Getting filament updates from tinermaq website')
        tinermaq_filaments = self.get_filaments_from_tinermaq()
        stored_filaments = self.load_filaments_from_store()

        logger.debug('Checking added filaments')
        added_filaments = []
        for filament in tinermaq_filaments:
            if filament not in stored_filaments:
                added_filaments.append(filament)

        logger.debug('Checking removed filaments')
        removed_filaments = []
        for filament in stored_filaments:
            if filament not in tinermaq_filaments:
                removed_filaments.append(filament)

        return added_filaments, removed_filaments

    @staticmethod
    def print_filaments_as_markdown(filaments: list[Filament], heading: str = ''):
        console = Console()
        if heading:
            console.print(f'{heading}', style='bold underline')
        for filament in filaments:
            console.print(Markdown(filament.as_markdown()))

    @staticmethod
    def notify_availability(filaments: list[Filament], to_email=settings.TO_EMAIL_ADDRESS):
        logger.info('Notifying filaments availability')
        message = render_message(
            dict(filaments=filaments, url=settings.URL), settings.AVAILABILITY_MSG_TEMPLATE
        )
        sg_handler = init_sendgrid()
        sg_handler.send(
            to=to_email, subject='Available Prusament at Tinermaq', msg=message, html=True
        )

    @staticmethod
    def notify_updates(
        added_filaments: list[Filament],
        removed_filaments: list[Filament],
        to_email=settings.TO_EMAIL_ADDRESS,
    ):
        logger.info('Notifying updates on filaments availability')
        message = render_message(
            dict(
                added_filaments=added_filaments,
                removed_filaments=removed_filaments,
                url=settings.URL,
            ),
            settings.UPDATES_MSG_TEMPLATE,
        )
        sg_handler = init_sendgrid()
        sg_handler.send(
            to=to_email,
            subject='Updates about Prusament at Tinermaq',
            msg=message,
            html=True,
        )
