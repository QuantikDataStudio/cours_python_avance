import json

from configuration import EconomieGouvConfiguration, DataGouvConfiguration


def lire_configuration():
    out = []
    with open("config.json", "r") as f:
        configuration = json.load(f)

    for config in configuration:
        config["sql_creation"] = retrouver_sql(config["fichier_sql"])
        if config["type_api"] == "economie_gouv":
            out.append(EconomieGouvConfiguration(**config))
        elif config["type_api"] == "data_gouv":
            out.append(DataGouvConfiguration(**config))
        else:
            raise ValueError(f"La clé type_api = {config['type_api']} n'est pas connue")

    return out


def retrouver_sql(nom_fichier):
    with open(f"sql/{nom_fichier}", "r") as f:
        return f.read()
