nodes_dict = {
    # chemical compound: (number (from 0 to 88), electronegativity, weight (u), radius (pm))
    # data obtained from: https://ptable.com/#Properties
    'H': (0, 2.20, 1.008, 53),
    'He': (1, None, 4.0026, 31),
    'Li': (2, 0.98, 6.94, 167),
    'Be': (3, 1.57, 9.0122, 112),
    'B': (4, 2.04, 10.81, 87),
    'C': (5, 2.55, 12.011, 67),
    'N': (6, 3.04, 14.007, 56),
    'O': (7, 3.44, 15.999, 48),
    'F': (8, 3.98, 18.998, 42),
    'Ne': (9, None, 20.180, 38),
    'Na': (10, 0.93, 22.990, 190),
    'Mg': (11, 1.31, 24.305, 145),
    'Al': (12, 1.61, 26.982, 118),
    'Si': (13, 1.90, 28.085, 111),
    'P': (14, 2.19, 30.974, 98),
    'S': (15, 2.58, 32.06, 88),
    'Cl': (16, 3.16, 35.45, 79),
    'Ar': (17, None, 39.948, 71),
    'K': (18, 0.82, 39.098, 243),
    'Ca': (19, 1.0, 40.078, 194),
    'Sc': (20, 1.36, 44.956, 184),
    'Ti': (21, 1.54, 47.867, 176),
    'V': (22, 1.63, 50.942, 171),
    'Cr': (23, 1.66, 51.996, 166),
    'Mn': (24, 1.55, 54.938, 161),
    'Fe': (25, 1.83, 55.845, 156),
    'Co': (26, 1.88, 58.933, 152),
    'Ni': (27, 1.91, 58.693, 149),
    'Cu': (28, 1.90, 63.546, 145),
    'Zn': (29, 1.65, 65.38, 142),
    'Ga': (30, 1.81, 69.723, 136),
    'Ge': (31, 2.01, 72.630, 125),
    'As': (32, 2.18, 74.922, 114),
    'Se': (33, 2.55, 78.971, 103),
    'Br': (34, 2.96, 79.904, 94),
    'Kr': (35, 3.0, 83.798, 88),
    'Rb': (36, 0.82, 85.468, 265),
    'Sr': (37, 0.95, 87.62, 219),
    'Y': (38, 1.22, 88.906, 212),
    'Zr': (39, 1.33, 91.224, 206),
    'Nb': (40, 1.6, 92.906, 198),
    'Mo': (41, 2.16, 95.95, 190),
    'Tc': (42, 1.9, 98.0, 183),
    'Ru': (43, 2.2, 101.07, 178),
    'Rh': (44, 2.28, 102.91, 173),
    'Pd': (45, 2.20, 106.42, 169),
    'Ag': (46, 1.93, 107.87, 165),
    'Cd': (47, 1.69, 112.41, 161),
    'In': (48, 1.78, 114.82, 156),
    'Sn': (49, 1.96, 118.71, 145),
    'Sb': (50, 2.05, 121.76, 133),
    'Te': (51, 2.1, 127.60, 123),
    'I': (52, 2.66, 126.90, 115),
    'Xe': (53, 2.6, 131.29, 108),
    'Cs': (54, 0.79, 132.91, 298),
    'Ba': (55, 0.89, 137.33, 253),
    'La': (56, 1.10, 138.91, None),
    'Ce': (57, 1.12, 140.12, None),
    'Pr': (58, 1.13, 140.91, 247),
    'Nd': (59, 1.14, 144.24, 206),
    'Pm': (60, None, 145.0, 205),
    'Sm': (61, 1.17, 150.36, 238),
    'Eu': (62, None, 151.96, 231),
    'Gd': (63, 1.20, 157.25, 233),
    'Tb': (64, None, 158.93, 225),
    'Dy': (65, 1.22, 162.50, 228),
    'Ho': (66, 1.23, 164.93, 226),
    'Er': (67, 1.24, 167.26, 226),
    'Tm': (68, 1.25, 168.93, 222),
    'Yb': (69, None, 173.05, 222),
    'Lu': (70, 1.27, 174.97, 217),
    'Hf': (71, 1.3, 178.49, 208),
    'Ta': (72, 1.5, 180.95, 200),
    'W': (73, 2.36, 183.84, 193),
    'Re': (74, 1.9, 186.21, 188),
    'Os': (75, 2.2, 190.23, 185),
    'Ir': (76, 2.2, 192.22, 180),
    'Pt': (77, 2.28, 195.08, 177),
    'Au': (78, 2.54, 196.97, 174),
    'Hg': (79, 2.0, 200.59, 171),
    'Th': (80, 1.62, 204.38, 156),
    'Pb': (81, 2.33, 207.2, 154),
    'Bi': (82, 2.02, 208.98, 143),
    'Ac': (83, 1.1, 227.0, None),
    'Th': (84, 1.3, 232.04, None),
    'Pa': (85, 1.5, 231.04, None),
    'U': (86, 1.38, 238.03, None),
    'Np': (87, 1.36, 237.0, None),
    'Pu': (88, 1.28, 244.0, None)
}