import os
LOYER_DATA = {}

path = os.path.abspath('data/indicateurs-loyers-appartements.csv')

with open(path, 'r', encoding='latin-1') as _loyer_f:
    lines = _loyer_f.readlines()
    for _l in lines:
        _l = _l.split(';')
        LOYER_DATA[_l[1]] = _l[7]


def get_loyer_moyen(insee_code):
    return LOYER_DATA.get(insee_code)