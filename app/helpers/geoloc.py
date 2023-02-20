import requests

API_GEOLIC_URL = 'https://geo.api.gouv.fr/communes'

def format_commune(commune):
    return {
        'code': commune.get('code'),
        'nom': commune.get('nom'),
        'code_postaux': commune.get('codesPostaux')
    }

def get_commune_by_dpt(dept: str):
    communes = requests.get(API_GEOLIC_URL, params={'codeDepartement': dept}).json()
    return [format_commune(_com) for _com in communes]
