import typer

from prusament.core import Handler
from prusament.utils import init_logger

app = typer.Typer(add_completion=False)
logger = init_logger()


@app.command()
def list(
    updates: bool = typer.Option(
        False, '--updates', '-u', show_default=False, help='List filament updates.'
    ),
):
    '''
    List available Prusa filaments.
    '''
    h = Handler()
    if updates:
        added_filaments, removed_filaments = h.get_filament_updates()
        print('ADDED FILAMENTS')
        for filament, url in added_filaments.items():
            print(f'{filament}: {url}')
        print('REMOVED FILAMENTS')
        for filament, url in removed_filaments.items():
            print(f'{filament}: {url}')
    else:
        filaments = h.get_filaments_from_tinermaq()
        for filament, url in filaments.items():
            print(f'{filament}: {url}')


@app.command()
def save():
    '''
    Save available Prusa filaments.
    '''
    h = Handler()
    h.get_filaments_from_tinermaq()
    h.save_filaments_to_store()


if __name__ == "__main__":
    app()
