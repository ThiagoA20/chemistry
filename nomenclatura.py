from atomos import atomos


def name(molecula):
    fm = molecula.fm
    nomenclatura = ""
    if "H" in fm:
        if "O" in fm:
            pass
        else:
            nomenclatura = f"Ácido {str(atomos[molecula.atomos[1]].abreviacao).title()}ídrico"
    molecula.nomenclatura = nomenclatura
    return molecula
