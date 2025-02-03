import duckdb


def stocker_dans_bdd(sql: str, fichier: str, bdd: str) -> None:
    print("Chargement dans la BDD")
    with duckdb.connect(bdd) as connection:
        connection.sql(sql)
        connection.sql('INSERT INTO consommation_brute_quotidienne_gaz_elec_raw '
                       f'SELECT * FROM read_json_auto("{fichier}")')


if __name__ == '__main__':
    print("ceci est un test de stocker_dans_bdd")
