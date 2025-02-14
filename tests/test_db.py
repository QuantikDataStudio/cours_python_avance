from contextlib import nullcontext as does_not_raise
import pytest
from duckdb import IOException

from bdd.db import stocker_dans_bdd


@pytest.mark.parametrize(
    "input_fixture, expectation",
    [
        ("dataset_correct_fixture", does_not_raise()),
        ("dataset_fichier_inexistant_fixture", pytest.raises(IOException))
    ]
)
def test_stocker_dans_bdd(request, test_db, input_fixture, expectation):
    fixture_val = request.getfixturevalue(input_fixture)
    with expectation:
        stocker_dans_bdd(
            sql=fixture_val["sql"],
            fichier=fixture_val["fichier"],
            bdd=fixture_val["bdd"],
            nom_table=fixture_val["nom_table"],
        )
        with test_db as conn:
            res = conn.sql(f"SELECT * from {fixture_val['nom_table']}").fetchall()
            assert res == fixture_val["expected"]
