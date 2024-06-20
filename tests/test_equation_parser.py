import pytest
from src.equation_parser import parse_equation

def test_parse_simple_equation():
    equation = "x + 3 = 0"
    expected = ('x', '+', 3, 0)
    assert parse_equation(equation) == expected
