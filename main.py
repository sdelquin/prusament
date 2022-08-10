import typer

from prusament.core import Handler

app = typer.Typer(add_completion=False)


@app.command()
def list(
    changed: bool = typer.Option(
        False, '--changed', '-c', show_default=False, help='List only changed filaments.'
    ),
):
    '''
    List available Prusa filaments.
    '''
    h = Handler()
    if changed:
        added_filaments, removed_filaments = h.get_changed_filaments()
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
