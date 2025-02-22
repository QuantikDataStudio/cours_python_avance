import logging
from contextlib import nullcontext as does_not_raise
from json import JSONDecodeError

import pytest

from utils.lecteur_configuration import lire_configuration, retrouver_sql


@pytest.mark.parametrize(
    "nom_fichier, resultat, expectation",
    [
        ("fixtures/sql/test_sql", "select_fixture", does_not_raise()),
        ("nom_fichier", None, pytest.raises(FileNotFoundError)),
    ],
)
def test_retrouver_sql(request, nom_fichier, resultat, expectation):
    with expectation:
        assert retrouver_sql(nom_fichier) == request.getfixturevalue(resultat)


@pytest.mark.parametrize(
    "nom_fichier, resultat, expectation",
    [
        ("fichier", None, pytest.raises(FileNotFoundError)),
        ("fixtures/config_vide.json", None, pytest.raises(JSONDecodeError)),
        ("fixtures/liste_vide.json", "empty_list_fixture", does_not_raise()),
        ("fixtures/economie_gouv.json", "economie_gouv_fixture", does_not_raise()),
        ("fixtures/data_gouv.json", "data_gouv_fixture", does_not_raise()),
        ("fixtures/data_type_inconnu.json", None, pytest.raises(ValueError)),
    ],
)
def test_lire_configuration(request, nom_fichier, resultat, expectation):
    with expectation:
        out = lire_configuration(nom_fichier, logging.getLogger("name"))
        assert out == request.getfixturevalue(resultat)
