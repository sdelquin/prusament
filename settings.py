from pathlib import Path

from prettyconf import config

PROJECT_DIR = Path(__file__).parent
PROJECT_NAME = PROJECT_DIR.name

URL = config(
    'URL', default='https://tinermaq.com/blog/categoria-producto/filamento/prusament/'
)
FILAMENT_CSS_PATH = config('FILAMENT_CSS_PATH', default='div.product_details>a')

FILAMENTS_DAT = config('FILAMENTS_DAT', default=PROJECT_DIR / 'filaments.csv', cast=Path)

LOGFILE = config('LOGFILE', default=PROJECT_DIR / (PROJECT_NAME + '.log'), cast=Path)
LOGFILE_SIZE = config('LOGFILE_SIZE', cast=float, default=1e6)
LOGFILE_BACKUP_COUNT = config('LOGFILE_BACKUP_COUNT', cast=int, default=3)
