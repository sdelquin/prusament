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

SENDGRID_APIKEY = config('SENDGRID_APIKEY')
SENDGRID_FROM_EMAIL = config('SENDGRID_FROM_EMAIL')
SENDGRID_FROM_NAME = config('SENDGRID_FROM_NAME')

TO_EMAIL_ADDRESS = config('TO_EMAIL_ADDRESS')
EMAIL_TEMPLATES_DIR = config(
    'EMAIL_TEMPLATES_DIR', default=PROJECT_DIR / 'templates', cast=Path
)
AVAILABILITY_MSG_TEMPLATE = config('AVAILABILITY_MSG_TEMPLATE', default='availability.md')
UPDATES_MSG_TEMPLATE = config('UPDATES_MSG_TEMPLATE', default='updates.md')
