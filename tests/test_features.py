"""Tests features functions."""

import pandas as pd
import pytest
from pandas.testing import assert_series_equal

from animal_shelter import features


def test_check_has_name():
    """Test if name of animal is correctly retrieved."""
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = features.check_has_name(s)
    expected = pd.Series([True, True, False])
    assert_series_equal(result, expected)


# def test_check_has_name_for_exceptions():
#     s = pd.Series(["3 centuries", "2 weeks", "5 years"])
#     with pytest.raises(IndexError) as exception:
#         features.compute_days_upon_outcome(s)
#     assert "exception message" in str(exception.value)


@pytest.fixture(scope="class")
def list_of_sexes():
    """List the test sex data."""
    return pd.Series(
        [
            "Neutered Male",
            "Intact Female",
            "Intact Male",
            "Spayed Female",
            "Batshit Crazy Male",
        ]
    )


class TestSexFunctions:
    """Create a class for test functions for the sex data."""

    def test_all_logical_sexes(self, list_of_sexes):
        """Test if string for sex is correctly retrieved."""
        result = features.get_sex(list_of_sexes)
        expected = pd.Series(["male", "female", "male", "female", "male"])
        assert_series_equal(result, expected)

    def test_all_logical_statuses(self, list_of_sexes):
        """Test if string for fixed or intact status is correctly retrieved."""
        result = features.get_neutered(list_of_sexes)
        expected = pd.Series(["fixed", "intact", "intact", "fixed", "unknown"])
        assert_series_equal(result, expected)
