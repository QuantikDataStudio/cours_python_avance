import abc

import requests


class Configuration(abc.ABC):
    def __init__(self, input_config):
        self.input_config = input_config

    @abc.abstractmethod
    def telecharger(self):
        pass


class EconomieGouvConfiguration(Configuration):
    def __init__(self, input_config):
        super().__init__(input_config)
        self.type_api = self.input_config["type_api"]
        self.dataset = self.input_config["dataset"]
        self.fichier_cible = self.input_config["fichier_cible"]
        self.fichier_sql = self.input_config["fichier_sql"]
        self.sql_creation = self.input_config["sql_creation"]
        self.select = self.input_config.get("select", [])

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
            r = requests.get(self.url.format(step=step, offset=offset))
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


class DataGouvConfiguration(Configuration):
    def __init__(self, input_config):
        super().__init__(input_config)
        self.type_api = self.input_config["type_api"]
        self.dataset = self.input_config["dataset"]
        self.fichier_cible = self.input_config["fichier_cible"]
        self.fichier_sql = self.input_config["fichier_sql"]
        self.sql_creation = self.input_config["sql_creation"]
        self.url = f"https://tabular-api.data.gouv.fr/api/resources/{self.dataset}/data/?Date__exact='2024-10-31'"

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
