import math_func
import pytest
import sys

@pytest.mark.parametrize('nu1, nu2, result',
                          [
    (7, 3, 10),
    (7, 13, 20),
    ('Hello ', 'World', 'Hello World'),
    (10.5, 26.5, 37)
                            ])
def test_add_parameterized(nu1, nu2, result):
    assert math_func.add(nu1, nu2) == result

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7, 13) == 20
    assert math_func.add(0) == 2
    assert math_func.add() == 9
    print(math_func.add(7, 2), '_==++')

@pytest.mark.number
def test_subtract():
    assert math_func.subtract() == 4
    assert math_func.subtract(7, 4) == 3
    assert math_func.subtract(7, 7) == 0
    assert math_func.subtract(7, -7) == 14
    assert math_func.subtract(7, 10) == -3

@pytest.mark.skipif(sys.version_info > (4, 1), reason="do not run add nr test")
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5, 10) == 50
    assert math_func.product(5, 6) == 30
    assert math_func.product(0, 2) == 0
    assert math_func.product(4, 0) == 0
    assert math_func.product(-3, -5) == 15
    assert math_func.product(-6, 7) == -42
    assert math_func.product(7, -7) == -49

@pytest.mark.number
def test_divide():
    assert math_func.divide(4, 2) == 2
    # assert math_funnc.divide(4, 0) == ZeroDivisionError
    assert math_func.divide(0, 6) == 0
    assert math_func.divide(10, -2) == -5
    assert math_func.divide(-15, 5) == -3
    assert math_func.divide(-20, -10) == 2

    assert math_func.divide(-21, 2) == -10.5
    assert math_func.divide(41, -2) == -20.5
    assert math_func.divide(65, 10) == 6.5

    assert math_func.divide(65, 10) >= 6.5
    assert math_func.divide(65, 10) < 6.6
    assert math_func.divide(65, 10) > 6.13

#       Testing string parameters into the same func

@pytest.mark.string
def test_add_string():
    assert math_func.add('Hey', '2') == 'Hey2'
    assert math_func.add('Heyo', ' !') == 'Heyo !'

    result = math_func.add('Hello', 'World')
    assert type(result) == str
    assert result == 'HelloWorld'
    assert 'Howdy' != result

@pytest.mark.string
def test_procuct_string():
    assert math_func.product('Hai') == 'HaiHai'
    result = math_func.product('Hello ', 3)
    assert result == 'Hello Hello Hello '
    assert type(result) is str
    assert 'Hell' in result