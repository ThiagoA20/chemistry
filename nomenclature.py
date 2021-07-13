from atoms import atoms


def name(molecula, nox):
    fm = molecula.fm
    nomenclature = ""
    if "H" in fm:
        if "O" in fm:
            pass
        else:
            nomenclature = f"{fm} = Hydro{str(atoms[molecula.atoms[1]].prefix)}ic acid"
    molecula.nomenclature = nomenclature
    return molecula
