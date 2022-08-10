import logzero
import typer

from prusament.core import Handler
from prusament.utils import init_logger

app = typer.Typer(add_completion=False)
logger = init_logger()


@app.command()
def list(
    quiet: bool = typer.Option(
        False, '--quiet', '-q', show_default=False, help='Run in quite mode.'
    ),
    updates: bool = typer.Option(
        False, '--updates', '-u', show_default=False, help='List filament updates.'
    ),
):
    '''
    List available Prusa filaments.
    '''
    logger.setLevel(logzero.ERROR if quiet else logzero.DEBUG)

    h = Handler()
    if updates:
        added_filaments, removed_filaments = h.get_filament_updates()
        if added_filaments:
            h.print_filaments_as_markdown(added_filaments, '✅ Added filaments')
        if removed_filaments:
            h.print_filaments_as_markdown(removed_filaments, '❌ Removed filaments')
    else:
        filaments = h.get_filaments_from_tinermaq()
        h.print_filaments_as_markdown(
            filaments, '📦 Available prusament filaments at tinermaq website'
        )


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
