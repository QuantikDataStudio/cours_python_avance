import duckdb


def stocker_dans_bdd(sql, fichier, bdd):
    print("Chargement dans la BDD")
    connection = duckdb.connect(bdd)
    connection.sql(sql)
    connection.sql('INSERT INTO consommation_brute_quotidienne_gaz_elec_raw '
                   f'SELECT * FROM read_json_auto("{fichier}")')
