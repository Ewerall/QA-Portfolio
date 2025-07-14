import pytest
import tkinter as tk
from calc_evil import ModernCalculator

@pytest.fixture
def calculator():
    root = tk.Tk()
    root.withdraw()
    calc = ModernCalculator(root)
    root.update_idletasks()
    root.update()
    yield calc
    root.destroy()

def test_start_state(calculator):
    assert calculator.get_display_value() == ''

def test_input(calculator):
    calculator.click_handler('5')
    assert calculator.get_display_value() == '5'

def test_plus(calculator):
    calculator.click_handler('2')
    calculator.click_handler('+')
    calculator.click_handler('3')
    calculator.click_handler('=')
    assert calculator.get_display_value() == '5'

def test_priority(calculator):
    calculator.click_handler('2')
    calculator.click_handler('+')
    calculator.click_handler('2')
    calculator.click_handler('*')
    calculator.click_handler('3')
    calculator.click_handler('=')
    assert calculator.get_display_value() == '8'

def test_error(calculator):
    calculator.click_handler('5')
    calculator.click_handler('+')
    calculator.click_handler('*')
    calculator.click_handler('=')
    assert "Ошибка" in calculator.get_display_value() 

def test_delete(calculator):
    calculator.click_handler('1')
    calculator.click_handler('2')
    calculator.click_handler('3')
    calculator.click_handler('⌫')
    assert calculator.get_display_value() == '12'

def test_clear(calculator):
    calculator.click_handler('1')
    calculator.click_handler('2')
    calculator.click_handler('3')
    calculator.click_handler('C')
    assert calculator.get_display_value() == ''

def test_decimal(calculator):
    calculator.click_handler('1')
    calculator.click_handler('.')
    calculator.click_handler('5')
    calculator.click_handler('+')
    calculator.click_handler('2')
    calculator.click_handler('.')
    calculator.click_handler('5')
    calculator.click_handler('=')
    assert calculator.get_display_value() == '4.0'

def test_percentage(calculator):
    calculator.click_handler('1')
    calculator.click_handler('0')
    calculator.click_handler('0')
    calculator.click_handler('+')
    calculator.click_handler('1')
    calculator.click_handler('0')
    calculator.click_handler('%')
    calculator.click_handler('=')
    assert calculator.get_display_value() == '110.0' #yep, this error

def test_resume(calculator):
    calculator.click_handler('2')
    calculator.click_handler('+')
    calculator.click_handler('2')
    calculator.click_handler('=')
    calculator.click_handler('+')
    calculator.click_handler('2')
    calculator.click_handler('=')
    assert calculator.get_display_value() == '6'
    
#Benchmark

def test_speed(benchmark, calculator):
    expression = '123*456-789+321/654'
    
    def setup():
        calculator.click_handler('C')
        for char in expression:
            calculator.click_handler(char)
    
    benchmark.pedantic(calculator.click_handler, args=('=',), setup=setup, rounds=50)
    assert benchmark.stats['mean'] < 0.1  # 100 ms

def test_button_speed(benchmark, calculator):
    benchmark(calculator.click_handler, '5')
    assert benchmark.stats['mean'] < 0.05  # 50 ms
    
@pytest.mark.parametrize("expression,expected", [
    ('2+2*2', '6'),
    ('10/3', '3.3333333333333335'),  
    ('5%', '0.05'),
    ('(2+3)*4', '20'),
    ('0.1+0.2', '0.3'), # <- here we have a problem with point
    ('999999*999999', '999998000001'),
])

def test_math_expressions(calculator, expression, expected):
    for char in expression:
        calculator.click_handler(char)
    calculator.click_handler('=')
    assert calculator.get_display_value() == expected

def test_code_injection(calculator):
    malicious = "__import__('os').system('rm -rf /')"
    for char in malicious:
        calculator.click_handler(char)
    calculator.click_handler('=')
    assert "Ошибка" in calculator.get_display_value()

def test_invalid_input(calculator):
    invalid_chars = ['a', '!', '@', '#', '$', '&', '_', ';']
    for char in invalid_chars:
        calculator.click_handler('C')
        calculator.click_handler(char)
        assert calculator.get_display_value() == ''
        
def test_scientific_notation(calculator):
    calculator.click_handler('1')
    for _ in range(20):
        calculator.click_handler('0')
    calculator.click_handler('*')
    
    calculator.click_handler('1')
    for _ in range(20):
        calculator.click_handler('0')
    calculator.click_handler('=')
    
    calculator.master.update()
    calculator.master.update_idletasks()
    result = calculator.get_display_value()
    
    assert any(c in result for c in ['e', 'E']) or "1e+40" in result, \
        f"Ожидалась научная запись, а получили {result}" #we dont have scientific notation
