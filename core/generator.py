import random
import re
from math import gcd

from core.chemicals import METALS, NON_METALS, ACIDS, BASES, LATEX_FORMULAS
from core.reaction import Reaction


def metal_oxide_formula(metal, ox_state):
    oxygen_state = 2
    lcm = (ox_state * oxygen_state) // gcd(ox_state, oxygen_state)
    metal_sub = lcm // ox_state
    oxygen_sub = lcm // oxygen_state
    metal_str = metal if metal_sub == 1 else f"{metal}_{metal_sub}"
    oxygen_str = "O" if oxygen_sub == 1 else f"O_{oxygen_sub}"
    return metal_str + oxygen_str, metal_sub, oxygen_sub

def metal_oxide_reaction():
    metal = random.choice(list(METALS.keys()))
    ox_state = random.choice(METALS[metal] if isinstance(METALS[metal], list) else [METALS[metal]])

    product, metal_sub, oxygen_sub = metal_oxide_formula(metal, ox_state)

    # Solve for coefficients
    # a*Mg + b*O2 -> c*MgO
    a = metal_sub
    b = oxygen_sub / 2  # O2 molecule has 2 O atoms
    c = 1

    # Multiply by 2 to get integers if necessary
    factor = 2
    a *= factor
    b *= factor
    c *= factor

    reactants = [metal, "O_2"]
    products = [product]
    solution = [int(a), int(b), int(c)]

    return Reaction(reactants, products, solution)


def metal_nonmetal_reaction():
    # Pick a metal
    metal = random.choice(list(METALS.keys()))
    metal_val = METALS[metal]
    if isinstance(metal_val, list):
        metal_val = random.choice(metal_val)

    # Pick a non-metal
    non_metal = random.choice(list(NON_METALS.keys()))
    non_metal_val = NON_METALS[non_metal]

    # Criss-cross subscripts
    metal_sub = abs(non_metal_val)
    non_metal_sub = abs(metal_val)
    divisor = gcd(metal_sub, non_metal_sub)
    metal_sub //= divisor
    non_metal_sub //= divisor

    # Formulas
    metal_formula = f"{metal}" + (f"_{metal_sub}" if metal_sub > 1 else "")

    # Wrap polyatomic ions in parentheses if subscript > 1
    if len(non_metal) > 1 and non_metal_sub > 1:
        non_metal_formula = f"({non_metal})_{non_metal_sub}"
    else:
        non_metal_formula = f"{non_metal}" + (f"_{non_metal_sub}" if non_metal_sub > 1 else "")
    
    product = f"{metal_formula}{non_metal_formula}"

    # Stoichiometric coefficients
    metal_coeff = metal_sub
    non_metal_coeff = non_metal_sub
    product_coeff = 1
    solution = [metal_coeff, non_metal_coeff, product_coeff]

    reactants = [metal, non_metal]
    products = [product]

    return Reaction(reactants, products, solution)



def combustion_reaction():
    # Random number of carbons in alkane
    n = random.randint(1, 12)  # C2 to C12
    alkane_formula = f"C_{{{n}}}H_{{{2*n+2}}}"

    # Stoichiometric coefficients (integer)
    coeff_alkane = 2
    coeff_O2 = 3*n + 1
    coeff_CO2 = 2*n
    coeff_H2O = 2*(n+1)

    reactants = [alkane_formula, "O_2"]
    products = ["CO_2", "H_2O"]
    solution = [coeff_alkane, coeff_O2, coeff_CO2, coeff_H2O]

    return Reaction(reactants, products, solution)


def generate_salt(acid: str, base: str):
    """
    Returns:
        salt (str, e.g. CaCl2)
        a = number of acidic H
        b = number of OH groups
    """
    import re
    from math import gcd

    # ---- Acid: H_aX ----
    m = re.match(r"H(\d*)([A-Za-z0-9()]+)", acid)
    if not m:
        raise ValueError(f"Cannot parse acid {acid}")
    a = int(m.group(1)) if m.group(1) else 1
    X = m.group(2)

    # ---- Base: B(OH)_b or BOH ----
    if "(OH)" in base:
        m2 = re.match(r"([A-Za-z]+)\(OH\)(\d*)", base)
        B = m2.group(1)
        b = int(m2.group(2)) if m2.group(2) else 1
    else:
        B = base.replace("OH", "")
        b = 1

    # ---- Criss-cross ----
    d = gcd(a, b)
    # ⚠ Corrected: metal subscript comes from acid H, non-metal from base OH
    sub_B = a // d
    sub_X = b // d

    # Wrap polyatomic ions in parentheses if subscript > 1
    if len(X) > 1 and sub_X > 1:
        X_str = f"({X}){sub_X}"
    else:
        X_str = f"{X}{sub_X if sub_X > 1 else ''}"

    salt = f"{B}{sub_B if sub_B > 1 else ''}{X_str}"

    return salt, a, b


def acid_base_reaction():
    acid = random.choice(list(ACIDS.keys()))
    base = random.choice(list(BASES.keys()))

    salt, a, b = generate_salt(acid, base)

    d = gcd(a, b)
    acid_coeff = b // d
    base_coeff = a // d
    salt_coeff = 1
    water_coeff = acid_coeff * a

    return Reaction(
        reactants=[acid, base],
        products=[salt, "H2O"],
        solution=[acid_coeff, base_coeff, salt_coeff, water_coeff],
    )


def generate_reaction(selected_types=None):
    # Default to all types if none selected
    if not selected_types:
        selected_types = ["metal_oxide", "combustion", "acid_base"]

    # Map keys to generator functions
    templates = []
    if "metal_oxide" in selected_types:
        templates.append(metal_oxide_reaction)
    if "combustion" in selected_types:
        templates.append(combustion_reaction)
    if "acid_base" in selected_types:
        templates.append(acid_base_reaction)
    if "metal_nonmetal" in selected_types:
        templates.append(metal_nonmetal_reaction)
        

    # Randomly pick one template
    template = random.choice(templates)
    return template()
