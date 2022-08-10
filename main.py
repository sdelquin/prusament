import typer

from prusament.core import get_filaments, load_filaments

app = typer.Typer(add_completion=False)


@app.command()
def list(
    new: bool = typer.Option(
        False, '--new', '-w', show_default=False, help='List only new filaments.'
    ),
):
    '''
    List available Prusa filaments.
    '''
    if new:
        old_filaments = load_filaments()
    else:
        old_filaments = set()
    current_filaments = set(get_filaments())
    new_filaments = current_filaments - old_filaments
    for filament in new_filaments:
        print(filament)


@app.command()
def save():
    '''
    Save available Prusa filaments.
    '''
    with open('filaments.dat', 'w') as f:
        for filament in get_filaments():
            f.write(filament + '\n')


if __name__ == "__main__":
    app()
