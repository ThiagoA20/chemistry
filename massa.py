from atomos import atomos


class molecula:
    def __init__(self, formula_molecular, massa_mol, quantidade_de_moleculas, atomos):
        self.fm = formula_molecular
        self.mm = massa_mol
        self.qm = quantidade_de_moleculas
        self.atomos = atomos
        self.mc = self.mm * self.qm
        self.nomenclatura = ""


num = ('1', '2', '3', '4', '5', '6', '7', '8', '9')


def massa_molecular(mol):
    fm = list(mol)
    molecula2 = []
    caracteres = []
    elementos = []
    mm = 0
    qm = 1

    # verificando se existem elementos com duas letras e agrupando eles
    for i in range(len(fm)):
        if i == len(fm) - 1:
            molecula2.append(fm[i])
        else:
            try:
                if str(fm[i + 1]).islower() and fm[i] not in num:
                    molecula2.append(fm[i] + fm[i + 1])
                    del(fm[i + 1])
                else:
                    molecula2.append(fm[i])
            except:
                pass

    # verificando se a quantidade de mols é maior do que 1
    try:
        if molecula2[0] in num:
            qm = int(molecula2[0])
            del(molecula2[0])
    except:
        pass

    # verificando se não há inconsistências na molécula (atomos que não existem)
    fm = ""
    for i in molecula2:
        if i not in num and i not in atomos:
            del i
        else:
            fm += i
            caracteres.append(i)

    # Calculando a massa molecular
    for atomo in range(len(caracteres)):
        for elemento in atomos:
            if caracteres[atomo] == elemento:
                ma = atomos[elemento].mass
                elementos.append(elemento)
                try:
                    if caracteres[atomo + 1] in num:
                        ma = int(ma) * int(caracteres[atomo + 1])
                except:
                    pass
                mm += int(ma)

    # retorna um objeto molécula contendo os dados processados
    return molecula(
        formula_molecular=fm,
        massa_mol=mm,
        quantidade_de_moleculas=qm,
        atomos=elementos,
    )
