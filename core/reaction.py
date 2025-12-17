import re
from core.chemicals import METALS, NON_METALS, ACIDS, BASES, LATEX_FORMULAS

class Reaction:
    def __init__(self, reactants, products, solution):
        """
        reactants: list of strings, chemical formulas with subscripts as _number (e.g., "H_2O")
        products: list of strings
        solution: list of integers, coefficients for each reactant + product
        """
        self.reactants = reactants
        self.products = products
        self.solution = solution


    def display(self, coeffs=None, hide_one=True):
        """
        Return LaTeX string of the reaction with coefficients.
        - coeffs: list of ints, same length as reactants + products
        - hide_one: if True, coefficient '1' will be omitted
        """
        total_compounds = len(self.reactants) + len(self.products)
        if coeffs is None:
            coeffs = [''] * total_compounds  # No coefficients yet

        # Convert coefficients: optionally hide 1
        coeffs_str = []
        for c in coeffs:
            if c == '':
                coeffs_str.append('')
            elif hide_one and c == 1:
                coeffs_str.append('')
            else:
                coeffs_str.append(str(c))

        # Left and right sides
        left = " + ".join(f"{c} {r}".strip() for c, r in zip(coeffs_str[:len(self.reactants)], self.reactants))
        right = " + ".join(f"{c} {p}".strip() for c, p in zip(coeffs_str[len(self.reactants):], self.products))

        return f"{left} \\rightarrow {right}"


    def latex_reactants(self):
        return [to_latex(r) for r in self.reactants]

    def latex_products(self):
        return [to_latex(p) for p in self.products]


def to_latex(formula: str) -> str:
    if formula in LATEX_FORMULAS:
        return LATEX_FORMULAS[formula]
    # Generic fallback for subscripts
    return re.sub(r"([A-Za-z\)])(\d+)", r"\1_{\2}", formula)
    


   