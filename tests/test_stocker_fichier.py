import pytest

from utils.stocker_fichier import stocker_fichier
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize(
    "input_fix, resultat, expectation",
    [
        ("input_incorrect_json_dump", None, pytest.raises(TypeError)),
        ("input_correct_json", '{"a": 1}{"a": 2}', does_not_raise()),
    ],
)
def test_stocker_fichier(request, input_fix, resultat, expectation, test_fichier):
    donnees = request.getfixturevalue(input_fix)
    with expectation:
        stocker_fichier(donnees, test_fichier)

        with open(test_fichier, "r") as f:
            assert resultat == f.read()
