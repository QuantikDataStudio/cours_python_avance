from dataclasses import dataclass

import requests


@dataclass
class EconomieGouvConfiguration:
    type_api: str
    dataset: str
    fichier_cible: str
    fichier_sql: str
    sql_creation: str
    select: list

    @property
    def url(self):
        if self.select:
            select_param = "%2C".join(self.select)
            return f"https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/{self.dataset}/records?select={select_param}&limit={{step}}&offset={{offset}}"
        else:
            return f"https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/{self.dataset}/records?limit={{step}}&offset={{offset}}"

    def telecharger(self):
        step = 100
        offset = 0
        toutes_les_data = []
        print("Télécharger les données")
        while True:
            r = requests.get(self.url.format(limit=step, offset=offset))
            r.raise_for_status()
            data = r.json()
            toutes_les_data += data['results']
            total_count = data['total_count']
            offset += step
            if total_count - offset <= 0:
                break
            if offset + step > 10000:
                break
        return toutes_les_data


class DataGouvConfiguration:
    type_api: str
    dataset: str
    fichier_cible: str
    fichier_sql: str
    sql_creation: str

    @property
    def url(self):
        return f"https://tabular-api.data.gouv.fr/api/resources/{self.dataset}/data/?Date__exact='2024-10-31'"

    def telecharger(self):
        toutes_les_data = []
        url = self.url
        print("Télécharger les données")
        while url:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
            toutes_les_data += data['data']
            url = data['links'].get("next")
        return toutes_les_data
