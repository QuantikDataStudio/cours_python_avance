import logging

import pytest

from configuration import EconomieGouvConfiguration, DataGouvConfiguration


@pytest.fixture
def fichier_non_existant():
    return "nom_fichier"


@pytest.fixture
def economie_gouv_fixture():
    return [
        EconomieGouvConfiguration(
            type_api="economie_gouv",
            dataset="dataset",
            fichier_cible="fichier_cible",
            fichier_sql="fixtures/sql/test_sql",
            sql_creation="SELECT",
            select=["id"],
            nom_table="nom_table"
        )
    ]


@pytest.fixture
def input_economie_gouv_fixture_select_vide():
    return {"type_api": "economie_gouv",
            "dataset": "dataset",
            "fichier_cible": "fichier_cible",
            "fichier_sql": "fixtures/sql/test_sql",
            "sql_creation": "SELECT",
            "nom_table": "nom_table",
            "select": []}


@pytest.fixture
def input_economie_gouv_fixture_sans_select():
    return {"type_api": "economie_gouv",
            "dataset": "dataset",
            "fichier_cible": "fichier_cible",
            "fichier_sql": "fixtures/sql/test_sql",
            "nom_table": "nom_table",
            "sql_creation": "SELECT"}


@pytest.fixture
def input_economie_gouv_fixture_avec_select():
    return {"type_api": "economie_gouv",
            "dataset": "dataset",
            "fichier_cible": "fichier_cible",
            "fichier_sql": "fixtures/sql/test_sql",
            "sql_creation": "SELECT",
            "nom_table": "nom_table",
            "select": ["id1", "id2"]}


@pytest.fixture
def input_data_gouv_fixture():
    return {"type_api": "data_gouv",
            "dataset": "dataset",
            "fichier_cible": "fichier_cible",
            "fichier_sql": "fixtures/sql/test_sql",
            "sql_creation": "SELECT",
            "nom_table": "nom_table",
            }

@pytest.fixture
def logger_fixture():
    return logging.getLogger("fixture")


@pytest.fixture
def data_gouv_fixture():
    return [
        DataGouvConfiguration(
            type_api="data_gouv",
            dataset="dataset",
            fichier_cible="fichier_cible",
            fichier_sql="fixtures/sql/test_sql",
            sql_creation="SELECT",
            nom_table="nom_table"
        )
    ]


@pytest.fixture
def empty_list_fixture():
    return []


@pytest.fixture
def select_fixture():
    return "SELECT"
