import typer

from prusament.core import get_filaments

app = typer.Typer(add_completion=False)


@app.command()
def list():
    '''
    List available Prusa filaments.
    '''
    for filament in get_filaments():
        print(filament)


@app.command()
def save():
    print('vamos')


if __name__ == "__main__":
    app()
