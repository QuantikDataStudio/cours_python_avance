from time import sleep
from urllib.error import HTTPError
from pydantic.dataclasses import dataclass

import requests


def requests_get(url: str, max_retries: int = 3) -> requests.Response:
    error_count = 0
    http_error_count = 0

    r = None
    while True:
        try:
            r = requests.get(url)
            r.raise_for_status()
            break
        except requests.exceptions.ConnectionError:
            error_count += 1
            if error_count > max_retries:
                raise
            else:
                sleep(10)
                continue
        except HTTPError:
            http_error_count += 1
            if http_error_count > max_retries:
                raise
            else:
                sleep(10)
                continue
    return r

@dataclass
class EconomieGouvConfiguration:
    type_api: str
    dataset: str
    fichier_cible: str
    fichier_sql: str
    sql_creation: str
    select: list
    nom_table: str

    @property
    def url(self) -> str:
        if self.select:
            select_param = "%2C".join(self.select)
            return f"https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/{self.dataset}/records?select={select_param}&limit={{step}}&offset={{offset}}"
        else:
            return f"https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/{self.dataset}/records?limit={{step}}&offset={{offset}}"

    def telecharger(self) -> list[dict]:
        step = 100
        offset = 0
        toutes_les_data = []
        print("Télécharger les données")
        while True:
            r = requests_get(self.url.format(step=step, offset=offset), 3)
            data = r.json()
            toutes_les_data += data['results']
            total_count = data['total_count']
            offset += step
            if total_count - offset <= 0:
                break
            if offset + step > 10000:
                break

        return toutes_les_data


@dataclass
class DataGouvConfiguration:
    type_api: str
    dataset: str
    fichier_cible: str
    fichier_sql: str
    sql_creation: str
    nom_table: str

    @property
    def url(self) -> str:
        return f"https://tabular-api.data.gouv.fr/api/resources/{self.dataset}/data/?Date__exact='2024-10-31'"

    def telecharger(self) -> list[dict]:
        toutes_les_data = []
        url = self.url
        print("Télécharger les données")
        while url:
            r = requests_get(url, 3)
            data = r.json()
            toutes_les_data += data['data']
            url = data['links'].get("next")
        return toutes_les_data
