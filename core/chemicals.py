# core/chemicals.py

# Metals and their common charges
METALS = {
    "Li": 1, "Na": 1, "K": 1, "Rb": 1, "Cs": 1, "Fr": 1,
    "Be": 2, "Mg": 2, "Ca": 2, "Sr": 2, "Ba": 2, "Ra": 2,
    "Al": 3, "Ga": 3, "In": 3, "Tl": 3,
    "Zn": 2, "Cd": 2, "Hg": 2,
    "Fe": [2, 3], "Cu": [1, 2], "Sn": [2, 4], "Pb": [2, 4]
}

# Non-metals and polyatomic ions
NON_METALS = {
    "F": -1, "Cl": -1, "Br": -1, "I": -1,
    "O": -2,
    "S": -2,
    "N": -3,
    "NO2": -1,
    "NO3": -1,
    "SO3": -2,
    "SO4": -2,
    "PO3": -3,
    "PO4": -3
}

# Acids and number of acidic protons
ACIDS = {
    "HCl": 1,
    "H2SO4": 2,
    "HNO3": 1,
    "H3PO4": 3
}

# Bases and number of OH per molecule
BASES = {
    "NaOH": 1,
    "KOH": 1,
    "Ca(OH)2": 2,
    "Mg(OH)2": 2
}

# Lookup table for LaTeX display
LATEX_FORMULAS = {
    "HCl": "HCl",
    "H2SO4": "H_2SO_4",
    "HNO3": "H_3NO_3",
    "H3PO4": "H_3PO_4",
    "H2O": "H_2O",
    "NaOH": "NaOH",
    "KOH": "KOH",
    "Ca(OH)2": "Ca(OH)_2",
    "Mg(OH)2": "Mg(OH)_2",
    "NO2": "NO_2",
    "NO3": "NO_3",
    "SO3": "SO_3",
    "SO4": "SO_4",
    "PO3": "PO_3",
    "PO4": "PO_4"
}
