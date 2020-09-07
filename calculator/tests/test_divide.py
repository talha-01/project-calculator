from src.calculator import divide
import pytest

def test_divide():
    result = divide(25, 5)
    assert result == 5

def test_divide_string():
    with pytest.raises(TypeError):
        divide('string', 4)