from src.calculator import multiply
import pytest 

def test_multiple():
    result = multiply(25, 5)
    assert result == 125

def test_multiple_string():
    with pytest.raises(TypeError):
        multiply('string', 4)