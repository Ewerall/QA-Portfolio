import pytest
import random
from calclogic import CalculatorLogic

@pytest.fixture
#Base test
def calculator():
    return CalculatorLogic()

def test_start_state(calculator):
    assert calculator.get_display_value() == ''

def test_input(calculator):
    calculator.click_handler('5')
    assert calculator.get_display_value() == '5'

def test_plus(calculator):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    calculator.click_handler(str(a))
    calculator.click_handler('+')
    calculator.click_handler(str(b))
    calculator.click_handler('=')
    assert calculator.get_display_value() == str(a + b)

def test_priority(calculator):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    calculator.click_handler(str(a))
    calculator.click_handler('+')
    calculator.click_handler(str(b))
    calculator.click_handler('*')
    calculator.click_handler(str(c))
    calculator.click_handler('=')
    assert calculator.get_display_value() == str(a + b * c)

def test_clear(calculator):
    a = random.randint(1, 9)
    calculator.click_handler(str(a))
    calculator.click_handler('C')
    assert calculator.get_display_value() == ''

def test_delete(calculator):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    calculator.click_handler(str(a))
    calculator.click_handler(str(b))
    calculator.click_handler('⌫')
    assert calculator.get_display_value() == str(a)

#Errors

def test_division_by_zero(calculator):
    a = random.randint(1, 9)
    calculator.click_handler(str(a))
    calculator.click_handler('/')
    calculator.click_handler('0')
    calculator.click_handler('=')
    assert calculator.get_display_value() == 'Ошибка'

def test_invalid_expression(calculator):
    a = random.randint(1, 9)
    calculator.click_handler(str(a))
    calculator.click_handler('+')
    calculator.click_handler('+')
    calculator.click_handler('=')
    assert calculator.get_display_value() == 'Ошибка'

def test_invalid_input(calculator):
    invalid_chars = ['a', '!', '@', '#', '$', '&', '_', ';']
    for char in invalid_chars:
        calculator.click_handler('C')
        calculator.click_handler(char)
        assert calculator.get_display_value() == ''

#math

@pytest.mark.parametrize("expression,expected", [
    ('2+2*2', '6'),
    ('10/3', '3.3333333333333335'),
    ('(2+3)*4', '20'),
    ('0.1+0.2', '0.3'),
    ('999999*999999', '999998000001'),
])

def test_math_expressions(calculator, expression, expected):
    for char in expression:
        calculator.click_handler(char)
    calculator.click_handler('=')
    result = calculator.get_display_value()
    try:
        assert float(result) == pytest.approx(float(expected), rel=1e-6)
    except ValueError:
        assert result == 'Ошибка'
        
def test_code_injection(calculator):
    malicious = "__import__('os').system('echo hacked')"
    for char in malicious:
        calculator.click_handler(char)
    calculator.click_handler('=')
    assert calculator.get_display_value() == 'Ошибка'

def test_dangerous_pattern(calculator):
    dangerous_inputs = [
        "__import__('os')",
        "system('rm -rf /')",
        "eval('1+1')"
    ]
    for expr in dangerous_inputs:
        calculator.click_handler(expr)
        calculator.click_handler('=')
        assert calculator.get_display_value() == 'Ошибка'
        calculator.click_handler('C')
        
def test_parentheses(calculator):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    calculator.click_handler('(')
    calculator.click_handler(str(a))
    calculator.click_handler('+')
    calculator.click_handler(str(b))
    calculator.click_handler(')')
    calculator.click_handler('*')
    calculator.click_handler(str(c))
    calculator.click_handler('=')
    assert calculator.get_display_value() == str((a+b)*c)

def test_decimal(calculator):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    calculator.click_handler(str(a))
    calculator.click_handler('.')
    calculator.click_handler(str(b))
    assert calculator.get_display_value() == str(a) + '.' + str(b)
    
def test_large_number(calculator):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    calculator.click_handler(str(a))
    calculator.click_handler('*')
    calculator.click_handler('*')    
    calculator.click_handler(str(b))
    calculator.click_handler('+')
    calculator.click_handler(str(c))
    calculator.click_handler('=')
    assert calculator.get_display_value() == str(a**b+c)

def test_long_expression(calculator):
    expr = '1+2*3-4/5+6*7-8/9'
    for char in expr:
        calculator.click_handler(char)
    calculator.click_handler('=')
    result = calculator.get_display_value()
    assert float(result) == pytest.approx(47.3111111111111, rel=1e-6)
    
def test_negative_number(calculator):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    calculator.click_handler('-')
    calculator.click_handler(str(a))
    calculator.click_handler('+')
    calculator.click_handler(str(b))
    calculator.click_handler('=')
    assert calculator.get_display_value() == str(-a+b)
    
def test_complex_expression(calculator):
    expression = "(1+2)*3-(4/2)+5**2"
    for char in expression:
        calculator.click_handler(char)
    calculator.click_handler('=')
    assert calculator.get_display_value() == '32'