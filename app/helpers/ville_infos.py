
import requests
from bs4 import BeautifulSoup

CITY_INFO_URL = 'https://www.bien-dans-ma-ville.fr'


def get_nbr_habitants_info(nom: str, insee_code: str):
    """
    """
    url = '{}/{}-{}/'.format(CITY_INFO_URL, nom.lower(), insee_code)
    res = requests.get(url)
    if res.status_code != 200:
        return "INCONNU"
    html_content = res.content
    soup = BeautifulSoup(html_content)
    bloc_chiffre = soup.find('table', class_='bloc_chiffre')
    if bloc_chiffre is None:
        return "INCONNU"
    nombre_hab = bloc_chiffre.find('tr').find_all('td')[1].text
    return nombre_hab
