import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

URL = 'https://tinermaq.com/blog/categoria-producto/filamento/prusament/'


response = requests.get(URL, headers={'User-Agent': generate_user_agent()})
soup = BeautifulSoup(response.text, 'html.parser')
for a in soup.select('div.product_details>a'):
    print(a.text)
    print(a['href'])
