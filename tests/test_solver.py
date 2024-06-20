import pytest
from src.solver import solve_equation

def test_solve_simple_equation():
    parsed_equation = ('x', '+', 3, 0)
    expected_solution = -3
    assert solve_equation(parsed_equation) == expected_solution
