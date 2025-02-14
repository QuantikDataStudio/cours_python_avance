import duckdb


def stocker_dans_bdd(sql, fichier, bdd, nom_table):
    print("Chargement dans la BDD")
    with duckdb.connect(bdd) as connection:
        connection.sql(sql)
        connection.sql(f'INSERT INTO {nom_table} '
                       f'SELECT * FROM read_json_auto("{fichier}")')


if __name__ == '__main__':
    print("ceci est un test de stocker_dans_bdd")
