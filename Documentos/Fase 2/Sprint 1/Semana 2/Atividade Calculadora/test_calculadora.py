import pytest
from calculadora import Calculadora

@pytest.mark.soma
@pytest.mark.parametrize("n1,n2,resultado",[
    (1, 2, 3),
    (-1,2,1)
])
def test_soma(n1,n2,resultado):
    calculadora = Calculadora(n1,n2)
    assert calculadora.soma(n1,n2) == resultado

@pytest.mark.sub
@pytest.mark.parametrize("n1,n2,resultado",[
    (5,3,2),
    (7,8,-1),
    (-2,-2,0)
])
def test_sub(n1,n2,resultado):
    calculadora = Calculadora(n1,n2)
    assert calculadora.sub(n1,n2) == resultado

@pytest.mark.mult
@pytest.mark.parametrize("n1,n2,resultado",[
    (8,8,64),
    (4,-2,-8),
    (0,3,0)
])
def test_mul(n1,n2,resultado):
    calculadora = Calculadora(n1,n2)
    assert calculadora.mul(n1,n2) == resultado

@pytest.mark.div
@pytest.mark.parametrize("n1,n2,resultado",[
    (6,2,3),
    (8,-4,-2)
])
def test_div(n1,n2,resultado):
    calculadora = Calculadora(n1,n2)
    assert calculadora.div(n1,n2) == resultado

@pytest.mark.div
def test_div_por_zero():
    calculadora = Calculadora(5,0)
    with pytest.raises(ZeroDivisionError) as exec_info:
        calculadora.div(5,0)
    assert "Impossível dividir um número por zero." in str(exec_info.value)

@pytest.mark.resto
@pytest.mark.parametrize("n1,n2,resultado",[
    (4,2,0),
    (-3,-2,-1)
])
def test_resto(n1,n2,resultado):
    calculadora = Calculadora(n1,n2)
    assert calculadora.resto(n1,n2) == resultado

@pytest.mark.resto
def test_resto_por_zero():
    calculadora = Calculadora(2,0)
    with pytest.raises(ZeroDivisionError) as exec_info:
        calculadora.resto(2,0)
    assert "Impossível dividir um número por zero, portanto não há resto" in str(exec_info.value)

@pytest.mark.pot
@pytest.mark.parametrize("n1,n2,resultado",[
    (4,2,16),
    (-2,2,4),
    (5,0,1)
])
def test_pot (n1,n2,resultado):
    calculadora = Calculadora(n1,n2)
    assert calculadora.pot(n1,n2) == resultado

@pytest.mark.raiz
@pytest.mark.parametrize("n1,n2,resultado",[
    (16,2,4),
    (0,3,0)
])
def test_raiz (n1,n2,resultado):
    calculadora = Calculadora(n1,n2)
    assert calculadora.raiz(n1,n2) == resultado

@pytest.mark.raiz
def test_raiz_por_zero():
    calculadora = Calculadora(2,0)
    with pytest.raises(ValueError) as exec_info:
        calculadora.raiz(2,0)
    assert "Não é possível tirar a raiz zero de um número" in str(exec_info.value)

@pytest.mark.raiz
def test_raiz_negativa():
    calculadora = Calculadora(-81,2)
    with pytest.raises(ValueError) as exec_info:
        calculadora.raiz(-81,2)
    assert "Não é possível tirar uma raiz negativa" in str(exec_info.value)