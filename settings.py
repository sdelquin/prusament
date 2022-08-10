from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path(__file__).parent
PROJECT_NAME = PROJECT_DIR.name

URL = config(
    'URL', default='https://tinermaq.com/blog/categoria-producto/filamento/prusament/'
)
FILAMENT_CSS_PATH = config('FILAMENT_CSS_PATH', default='div.product_details>a')

FILAMENTS_DAT = config('FILAMENTS_DAT', default=PROJECT_DIR / 'filaments.dat', cast=Path)
