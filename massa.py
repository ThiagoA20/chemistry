import time

class element:
    def __init__(self, name, num, mass):
        self.name = name,
        self.num = num,
        self.mass = mass


massa = {
    "H": element("Hidrogênio", 1, 1),
    "He": element("Hélio", 2, 4),
    "Li": element("Lítio", 3, 7),
    "Be": element("Berílio", 4, 9),
    "B": element("Boro", 5, 11),
    "C": element("Carbono", 6, 12),
    "N": element("Nitrogênio", 7, 14),
    "O": element("Oxigênio", 8, 16),
    "F": element("Flúor", 9, 19),
    "Ne": element("Neônio", 10, 20),
    "Na": element("Sódio", 11, 23),
    "Mg": element("Magnésio", 12, 24),
    "Al": element("Alumínio", 13, 27),
    "Si": element("Silício", 14, 28),
    "P": element("Fósforo", 15, 31),
    "S": element("Enxofre", 16, 32),
    "Cl": element("Cloro", 17, 35.5),
    "Ar": element("Argônio", 18, 39.9),
    "K": element("Potássio", 19, 39),
    "Ca": element("Cálcio", 20, 40),
    "Sc": element("Escândio", 21, 45),
    "Ti": element("Titânio", 22, 48),
    "V": element("Vanádio", 23, 51),
    "Cr": element("Cromo", 24, 52),
    "Mn": element("Manganês", 25, 55),
    "Fe": element("Ferro", 26, 56),
    "Co": element("Cobalto", 27, 58.9),
    "Ni": element("Níquel", 28, 58.7),
    "Cu": element("Cobre", 29, 63.5),
    "Zn": element("Zinco", 30, 65.5),
    "Ga": element("Gálio", 31, 70),
    "Ge": element("Germânio", 32, 72.5),
    "As": element("Arsênio", 33, 75),
    "Se": element("Selênio", 34, 79),
    "Br": element("Bromo", 35, 80),
    "Kr": element("Criptônio", 36, 84),
    "Rb": element("Rubídio", 37, 85.5),
    "Sr": element("Estrôncio", 38, 87.5),
    "Y": element("Ítrio", 39, 89),
    "Zr": element("Zircônio", 40, 91),
    "Nb": element("Nióbio", 41, 93),
    "Mo": element("Molibdênio", 42, 96),
    "Tc": element("Tecnécio", 43, 98),
    "Ru": element("Rutênio", 44, 101),
    "Rh": element("Ródio", 45, 103),
    "Pd": element("Paládio", 46, 106.5),
    "Ag": element("Prata", 47, 108),
    "Cd": element("Cádmio", 48, 112.5),
    "In": element("Índio", 49, 115),
    "Sn": element("Estanho", 50, 118.5),
    "Sb": element("Antimônio", 51, 121.5),
    "Te": element("Telúrio", 52, 128.5),
    "I": element("Iodo", 53, 127),
    "Xe": element("Xenônio", 54, 131),
    "Cs": element("Césio", 55, 133),
    "Ba": element("Bário", 56, 137),
    "La": element("Lantânio", 57, 139),
    "Ce": element("Cério", 58, 140),
    "Pr": element("Praseodímio", 59, 141),
    "Nd": element("Neodímio", 60, 144),
    "Pm": element("Promécio", 61, 145),
    "Sm": element("Samário", 62, 150),
    "Eu": element("Európio", 63, 152),
    "Gd": element("Gadolínio", 64, 157),
    "Tb": element("Térbio", 65, 159),
    "Dy": element("Disprósio", 66, 162.5),
    "Ho": element("Hólmio", 67, 165),
    "Er": element("Érbio", 68, 167),
    "Tm": element("Túlio", 69, 169),
    "Yb": element("Itérbio", 70, 173),
    "Lu": element("Lutécio", 71, 175),
    "Hf": element("Háfnio", 72, 178.5),
    "Ta": element("Tântalo", 73, 181),
    "W": element("Tungstênio", 74, 184),
    "Re": element("Rênio", 75, 186),
    "Os": element("Ósmio", 76, 190),
    "Ir": element("Irídio", 77, 192),
    "Pt": element("Platina", 78, 195),
    "Au": element("Ouro", 79, 197),
    "Hg": element("Mercúrio", 80, 200.5),
    "Tl": element("Tálio", 81, 204),
    "Pb": element("Chumbo", 82, 207),
    "Bi": element("Bismuto", 83, 209),
    "Po": element("Polônio", 84, 210),
    "At": element("Ástato", 85, 210),
    "Rn": element("Radônio", 86, 220),
    "Fr": element("Frâncio", 87, 223),
    "Ra": element("Rádio", 88, 226),
    "Ac": element("Actínio", 89, 227),
    "Th": element("Tório", 90, 232),
    "Pa": element("Protactínio", 91, 231),
    "U": element("Urânio", 92, 238),
    "Np": element("Netúnio", 93, 237),
    "Pu": element("Plutônio", 94, 244),
    "Am": element("Amerício", 95, 243),
    "Cm": element("Cúrio", 96, 247),
    "Bk": element("Berquélio", 97, 247),
    "Cf": element("Califórnio", 98, 251),
    "Es": element("Einsténio", 99, 252),
    "Fm": element("Férmio", 100, 257),
    "Md": element("Mendelévio", 101, 258),
    "No": element("Nobélio", 102, 259),
    "Lr": element("Laurêncio", 103, 262),
    "Rf": element("Rutherfórdio", 104, 261),
    "Db": element("Dúbnio", 105, 262),
    "Sg": element("Seabórgio", 106, 266),
    "Bh": element("Bóhrio", 107, 264),
    "Hs": element("Hássio", 108, 277),
    "Mt": element("Meitnério", 109, 268),
    "Ds": element("Darmstádio", 110, 271),
    "Rg": element("Roentgênio", 111, 272),
    "Cn": element("Copernício", 112, 277),
    "Nh": element("Nihônio", 113, 286),
    "Fl": element("Fleróvio", 114, 289),
    "Mc": element("Moscóvio", 115, 288),
    "Lv": element("Livermório", 116, 293),
    "Ts": element("Tenessino", 117, 294),
    "Og": element("Oganessônio", 118, 294)
}

num = ('1', '2', '3', '4', '5', '6', '7', '8', '9')


def massa_molecular(molecula):
    molecula = list(molecula)
    molecula2 = []
    for i in range(len(molecula)):
        if i == len(molecula) - 1:
            molecula2.append(molecula[i])
        else:
            try:
                if str(molecula[i + 1]).islower() and molecula[i] not in num:
                    molecula2.append(molecula[i] + molecula[i + 1])
                    del(molecula[i + 1])
                else:
                    molecula2.append(molecula[i])
            except:
                pass
    mm = 0
    qm = 1
    elementos = []
    try:
        if molecula2[0] in num:
            qm = int(molecula2[0])
            del(molecula2[0])
    except:
        pass
    molecula = ""
    for i in molecula2:
        if i not in num and i not in massa:
            del i
        else:
            molecula += i
    for atomo in range(len(molecula)):
        for elemento in massa:
            if molecula[atomo] == elemento:
                elementos.append(elemento)
                ma = massa[elemento].mass
                try:
                    if molecula[atomo + 1] in num:
                        ma = int(ma) * int(molecula[atomo + 1])
                except:
                    pass
                mm += int(ma)
    print(f"\nMolécula: {molecula}")
    print(f"Massa Molecular: {mm}")
    print(f"Quantidade de moléculas: {qm}")
    print(f"Átomos: {elementos}")
    if qm != 1:
        print(f"M.M. * Q.M. = {mm * qm}")


while True:
    print(f"---------- Operação ----------\n\n1 - Massa Molecular\n2 - ...")
    number = int(input("\nDigite um número: "))
    if number == 1:
        molecula = str(input("Digite uma molécula: "))
        massa_molecular(molecula)
    time.sleep(5)
    c = str(input("\nDeseja continuar? (S/N): "))
    if c.lower() == "s":
        pass
    else:
        break
