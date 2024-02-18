import pytest

from src.practica_3 import es_factorial

def test_factorial_1():
    assert es_factorial(1,1)==True
def test_envia_TypeError():
    with pytest.raises(TypeError):
        es_factorial(1.1,5.3)
def test_envia_ValueError():
    with pytest.raises(ValueError):
        es_factorial(-1,-1)    
def test_factorial_5():
    assert es_factorial(5,120)==True