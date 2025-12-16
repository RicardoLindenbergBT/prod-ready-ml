"""Tests data functions."""
import pytest

from animal_shelter import data


def test_convert_camel_case():
    """Test if camel case or other is correctly changed to snake case."""
    assert data.convert_camel_case("CamelCase") == "camel_case"
    assert data.convert_camel_case("CamelCASE") == "camel_case"
    assert data.convert_camel_case("camel-case") != "camel_case"

def test_for_exceptions():
    """Test if snake case conversion raises exceptions when expected."""
    with pytest.raises(TypeError):
        data.convert_camel_case(123)