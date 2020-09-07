from src.calculator import subtract
import pytest 

def test_subtract():
    result = subtract(25, 5)
    assert result == 20

def test_subtract_string():
    with pytest.raises(TypeError):
        subtract('string', 4)