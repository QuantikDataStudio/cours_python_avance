import pytest
from utils.lecteur_configuration import retrouver_sql


def test_retrouver_sql_fichier_existant():
    res = retrouver_sql("test_sql")
    res_attendu = "SELECT"
    assert res == res_attendu


def test_retrouver_sql_fichier_inexistant():
    with pytest.raises(FileNotFoundError):
        retrouver_sql("nom_fichier")
