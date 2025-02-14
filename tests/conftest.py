import logging
import os

import duckdb
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
            select=["id"]
        )
    ]


@pytest.fixture
def input_economie_gouv_fixture_select_vide():
    return {"type_api": "economie_gouv",
            "dataset": "dataset",
            "fichier_cible": "fichier_cible",
            "fichier_sql": "fixtures/sql/test_sql",
            "sql_creation": "SELECT",
            "select": []}


@pytest.fixture
def input_economie_gouv_fixture_sans_select():
    return {"type_api": "economie_gouv",
            "dataset": "dataset",
            "fichier_cible": "fichier_cible",
            "fichier_sql": "fixtures/sql/test_sql",
            "sql_creation": "SELECT"}


@pytest.fixture
def input_economie_gouv_fixture_avec_select():
    return {"type_api": "economie_gouv",
            "dataset": "dataset",
            "fichier_cible": "fichier_cible",
            "fichier_sql": "fixtures/sql/test_sql",
            "sql_creation": "SELECT",
            "select": ["id1", "id2"]}


@pytest.fixture
def input_data_gouv_fixture():
    return {"type_api": "data_gouv",
            "dataset": "dataset",
            "fichier_cible": "fichier_cible",
            "fichier_sql": "fixtures/sql/test_sql",
            "sql_creation": "SELECT"
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
        )
    ]


@pytest.fixture
def empty_list_fixture():
    return []


@pytest.fixture
def select_fixture():
    return "SELECT"


@pytest.fixture
def test_db():
    yield duckdb.connect("random_db.db")
    os.unlink("random_db.db")


@pytest.fixture
def dataset_correct_fixture():
    return {
        "sql": "CREATE TABLE IF NOT EXISTS table_test (col1 INT)",
        "fichier": "fixtures/donnees_tests.json",
        "bdd": "random_db.db",
        "nom_table": "table_test",
        "expected": [(1,), (2,)]
    }

@pytest.fixture
def dataset_fichier_inexistant_fixture():
    return {
        "sql": "CREATE TABLE IF NOT EXISTS table_test (col1 INT)",
        "fichier": "donnees_tests.json",
        "bdd": "random_db.db",
        "nom_table": "table_test",
        "expected": [(1,), (2,)]
    }
