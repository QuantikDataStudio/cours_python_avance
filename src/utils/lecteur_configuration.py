import json

from configuration import EconomieGouvConfiguration, DataGouvConfiguration


def lire_configuration(logger):
    out = []

    logger.info("Lecture du fichier config.json")
    with open("config.json", "r") as f:
        configuration = json.load(f)

    for config in configuration:
        logger.debug(f"Chargement du SQL depuis {config['fichier_sql']}")
        config["sql_creation"] = retrouver_sql(config["fichier_sql"])

        if config["type_api"] == "economie_gouv":
            logger.debug("Trouvé config pour API EconomieGouv")
            out.append(EconomieGouvConfiguration(**config))

        elif config["type_api"] == "data_gouv":
            logger.debug("Trouvé config pour API DataGouv")
            out.append(DataGouvConfiguration(**config))

        else:
            logger.error(f"Le type API {config['type_api']} n'est pas connu")
            raise ValueError(f"La clé type_api = {config['type_api']} n'est pas connue")

    return out


def retrouver_sql(nom_fichier):
    with open(f"sql/{nom_fichier}", "r") as f:
        return f.read()
