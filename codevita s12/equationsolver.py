from itertools import product
def parse_equation(equation):
    parts = equation.split("<=")
    coefficients = parts[0].strip()
    limit = int(parts[1].strip())
    variables = [0, 0, 0, 0]
    for term in coefficients.split("+"):
        coeff, var = term.strip().split("x")[0], term.strip()[-1]
        idx = ord(var) - ord('w')
        variables[idx] = int(coeff)
    return variables, limit
def count_results(equation1, equation2, R):
    coeff1, limit1 = parse_equation(equation1)
    coeff2, limit2 = parse_equation(equation2)
    results = set()
    for x, y, z, w in product(range(R + 1), repeat=4):
        if x + y + z + w <= R:
            value1 = coeff1[0]*x + coeff1[1]*y + coeff1[2]*z + coeff1[3]*w
            value2 = coeff2[0]*x + coeff2[1]*y + coeff2[2]*z + coeff2[3]*w
            if value1 <= limit1 and value2 <= limit2 and value1 == value2:
                results.add(value1)
    return len(results)
equation1 = input().strip()
equation2 = input().strip()
R = int(input().strip())
print(count_results(equation1, equation2, R))