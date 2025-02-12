import logging
from json import JSONDecodeError

import pytest

from configuration import EconomieGouvConfiguration, DataGouvConfiguration
from utils.lecteur_configuration import retrouver_sql, lire_configuration


def test_retrouver_sql_fichier_existant():
    res = retrouver_sql("fixtures/sql/test_sql")
    res_attendu = "SELECT"
    assert res == res_attendu


def test_retrouver_sql_fichier_inexistant():
    with pytest.raises(FileNotFoundError):
        retrouver_sql("nom_fichier")


def test_lire_configuration_fichier_non_existant():
    with pytest.raises(FileNotFoundError):
        lire_configuration("fichier", logging.getLogger("name"))


def test_lire_configuration_fichier_vide():
    with pytest.raises(JSONDecodeError):
        lire_configuration("fixtures/config_vide.json", logging.getLogger("name"))


def test_lire_configuration_liste_vide():
    out = lire_configuration("fixtures/liste_vide.json", logging.getLogger("name"))
    assert out == []


def test_lire_configuration_economie_gouv():
    out = lire_configuration("fixtures/economie_gouv.json", logging.getLogger("name"))
    assert isinstance(out, list)
    assert len(out) == 1
    assert isinstance(out[0], EconomieGouvConfiguration)
    assert out[0].dataset == "dataset"
    assert out[0].fichier_cible == "fichier_cible"
    assert out[0].fichier_sql == "fixtures/sql/test_sql"
    assert out[0].select == ["id"]


def test_lire_configuration_data_gouv():
    out = lire_configuration("fixtures/data_gouv.json", logging.getLogger("name"))
    assert isinstance(out, list)
    assert len(out) == 1
    assert isinstance(out[0], DataGouvConfiguration)
    assert out[0].dataset == "dataset"
    assert out[0].fichier_cible == "fichier_cible"
    assert out[0].fichier_sql == "fixtures/sql/test_sql"


def test_lire_configuration_type_inconnu():
    with pytest.raises(ValueError):
        lire_configuration("fixtures/data_type_inconnu.json", logging.getLogger("name"))
