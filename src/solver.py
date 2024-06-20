def solve_equation(parsed_equation):
    variable, operator, number, result = parsed_equation
    if operator == '+':
        solution = -number
    elif operator == '-':
        solution = number
    else:
        raise ValueError(f"Unknown operator {operator}")
    return solution
