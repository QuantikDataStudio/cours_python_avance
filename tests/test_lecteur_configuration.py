from contextlib import contextmanager
import logging
from json import JSONDecodeError

import pytest

from configuration import EconomieGouvConfiguration, DataGouvConfiguration
from utils.lecteur_configuration import retrouver_sql, lire_configuration

@contextmanager
def does_not_raise():
    yield

@pytest.mark.parametrize(
    "nom_fichier, resultat, expectation",
    [
        ("fixtures/sql/test_sql", "SELECT", does_not_raise()),
        ("nom_fichier", None, pytest.raises(FileNotFoundError))
    ]
)
def test_retrouver_sql(nom_fichier, resultat, expectation):
    with expectation:
        assert retrouver_sql(nom_fichier) == resultat


@pytest.mark.parametrize(
    "nom_fichier, resultat, expectation",
    [
        ("fichier", None, pytest.raises(FileNotFoundError)),
        ("fixtures/config_vide.json", None, pytest.raises(JSONDecodeError)),
        ("fixtures/liste_vide.json", [], does_not_raise()),
        ("fixtures/economie_gouv.json", [
            EconomieGouvConfiguration(
                type_api="economie_gouv",
                dataset="dataset",
                fichier_cible="fichier_cible",
                fichier_sql="fixtures/sql/test_sql",
                sql_creation="SELECT",
                select=["id"],
                nom_table="nom_table"
            )
        ], does_not_raise()),
        ("fixtures/data_gouv.json", [
            DataGouvConfiguration(
                type_api="data_gouv",
                dataset="dataset",
                fichier_cible="fichier_cible",
                fichier_sql="fixtures/sql/test_sql",
                sql_creation="SELECT",
                nom_table="nom_table"
            )
        ], does_not_raise()),
        ("fixtures/data_type_inconnu.json", None, pytest.raises(ValueError)),
    ]
)
def test_lire_configuration(nom_fichier, resultat, expectation):
    with expectation:
        out = lire_configuration(nom_fichier, logging.getLogger("name"))
        assert out == resultat
