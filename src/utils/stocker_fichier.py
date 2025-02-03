import json


def stocker_fichier(donnees: list, nom_fichier: str) -> None:
    print("Stockage dans le fichier")

    with open(nom_fichier, "w") as f:
        for line in donnees:
            json.dump(line, f)
