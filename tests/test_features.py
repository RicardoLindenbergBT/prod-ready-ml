import pandas as pd

from pandas.testing import assert_series_equal

from animal_shelter import features

import pytest

def test_check_has_name():
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = features.check_has_name(s)
    expected = pd.Series([True, True, False])
    assert_series_equal(result, expected)

def test_check_has_name_for_exceptions():
    s = pd.Series(["Ivo", "Henk", None])
    with pytest.raises(Exception) as exception:
        features.check_has_name(s)
    assert "exception message" in str(exception.value)

import pytest

@pytest.fixture(scope="class")
def list_of_sexes():
    return pd.Series(["Neutered Male", "Intact Female", "Intact Male", "Spayed Female", "Batshit Crazy Male"])

class TestSexFunctions:
    def test_all_logical_sexes(self, list_of_sexes):
        result = features.get_sex(list_of_sexes)
        expected = pd.Series(["male", "female", "male", "female", "male"])
        assert_series_equal(result, expected)

    def test_all_logical_statuses(self, list_of_sexes):
        result = features.get_neutered(list_of_sexes)
        expected = pd.Series(["fixed", "intact", "intact", "fixed", "unknown"])
        assert_series_equal(result, expected)