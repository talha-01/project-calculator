from src.calculator import add
import pytest 

def test_add():
    result = add(5, 25)
    assert result == 30

def test_add_string():
    with pytest.raises(TypeError):
        add('string', 4)