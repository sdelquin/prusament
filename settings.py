from prettyconf import config

URL = config(
    'URL', default='https://tinermaq.com/blog/categoria-producto/filamento/prusament/'
)
FILAMENT_CSS_PATH = config('FILAMENT_CSS_PATH', default='div.product_details>a')
