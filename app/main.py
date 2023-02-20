from typing import Union

from fastapi import FastAPI

from helpers.geoloc import get_commune_by_dpt
from helpers.loyer import get_loyer_moyen
from helpers.ville_infos import get_nbr_habitants_info


app = FastAPI()


@app.get("/api/v1/villes/")
def cities(dept: Union[str, None] = None, loyer_max: Union[int, None] = None, surface: Union[int, None] = None):
    """
    """
    communes = get_commune_by_dpt(dept=dept)
    output = []
    for _com in communes:
        loyer_moyen_par_m2 = float(
            get_loyer_moyen(
                _com.get('code')).replace(',', '.')
        )
        loyer_moyen_surface = surface * loyer_moyen_par_m2
        if loyer_moyen_surface <= loyer_max:
            nb_h = get_nbr_habitants_info(nom=_com.get('nom'), insee_code=_com.get('code'))
            _com.update(
                {
                    'loyer_moyen': loyer_moyen_par_m2,
                    'habitants': nb_h
                }
            )
            output.append(_com)
    return {"villes": output}
