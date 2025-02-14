from utils.stocker_fichier import stocker_fichier
from utils.lecteur_configuration import lire_configuration
from bdd.db import stocker_dans_bdd

fichier_base_de_donnees = "../data/bdd_cours_python_avance"


if __name__ == '__main__':

    configuration = lire_configuration()

    for config in configuration:
        resultat = config.telecharger()
        stocker_fichier(resultat, config.fichier_cible)
        nom_table = config.fichier_sql.split("/")[-1].split(".")[0]
        stocker_dans_bdd(config.sql_creation, config.fichier_cible, fichier_base_de_donnees, nom_table)
