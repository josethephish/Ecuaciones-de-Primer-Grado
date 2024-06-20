def parse_equation(equation):
    # Supone que la ecuación siempre está en el formato "x + 3 = 0"
    left_side, right_side = equation.split('=')
    right_side = right_side.strip()
    assert right_side == '0'

    parts = left_side.split()
    assert len(parts) == 3  # x, operador, número

    variable = parts[0]
    operator = parts[1]
    number = int(parts[2])

    return (variable, operator, number, int(right_side))
