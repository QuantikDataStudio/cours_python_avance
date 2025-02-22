from contextlib import nullcontext as does_not_raise

import pytest
from pydantic import ValidationError

from configuration import DataGouvConfiguration, EconomieGouvConfiguration


@pytest.mark.parametrize(
    "economie_gouv_fix, expectation",
    [
        ("input_economie_gouv_fixture_sans_select", pytest.raises(ValidationError)),
        ("input_economie_gouv_fixture_select_vide", does_not_raise()),
        ("input_economie_gouv_fixture_avec_select", does_not_raise()),
    ],
)
def test_economie_gouv_configuration(request, economie_gouv_fix, expectation):
    input_cfg = request.getfixturevalue(economie_gouv_fix)
    with expectation:
        econ_gouv_cfg = EconomieGouvConfiguration(**input_cfg)
        if input_cfg["select"]:
            url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/dataset/records?select=id1%2Cid2&limit={step}&offset={offset}"
            assert (
                econ_gouv_cfg.url == url
            ), f"L'URL {econ_gouv_cfg.url} ne matche pas nos attentes"
        else:
            url = "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/dataset/records?limit={step}&offset={offset}"
            assert (
                econ_gouv_cfg.url == url
            ), f"L'URL {econ_gouv_cfg.url} ne matche pas nos attentes"


def test_data_gouv_configuration(input_data_gouv_fixture):
    data_gouv_cfg = DataGouvConfiguration(**input_data_gouv_fixture)
    url = "https://tabular-api.data.gouv.fr/api/resources/dataset/data/?Date__exact='2024-10-31'"
    assert (
        data_gouv_cfg.url == url
    ), f"L'URL {data_gouv_cfg.url} ne matche pas nos attentes"
