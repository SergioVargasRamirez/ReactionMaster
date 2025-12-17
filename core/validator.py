import math

def normalize(coeffs):
    gcd = coeffs[0]
    for c in coeffs[1:]:
        gcd = math.gcd(gcd, c)
    return [c // gcd for c in coeffs]

def validate_solution(user_input, correct):
    try:
        user = [int(x.strip()) for x in user_input.split(",")]
    except ValueError:
        return False
    if len(user) != len(correct):
        return False
    return normalize(user) == normalize(correct)

