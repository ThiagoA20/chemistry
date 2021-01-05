from atoms import atoms


class molecule:
    def __init__(self, molecular_formula, molecule_mass, molecules_amount, atomos, mol_of_elements):
        self.fm = molecular_formula
        self.mm = molecule_mass
        self.qm = molecules_amount
        self.atoms = atomos
        self.mol_of_elements = mol_of_elements
        self.mc = self.mm * self.qm
        self.nomenclature = ""


num = ('1', '2', '3', '4', '5', '6', '7', '8', '9')


def molecular_mass(mol):
    fm = list(mol)
    molecula2 = []
    characters = []
    elements = []
    mol_of_elements = {}
    mm = 0
    qm = 1

    # checking for two letter elements and grouping them together
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

    # checking if the number of moles is greater than 1
    try:
        if molecula2[0] in num:
            qm = int(molecula2[0])
            del(molecula2[0])
    except:
        pass

    # checking that there are no inconsistencies in the molecule (atoms that do not exist)
    fm = ""
    for i in molecula2:
        if i not in num and i not in atoms:
            del i
        else:
            fm += i
            characters.append(i)

    # Calculating molecular mass
    for atom in range(len(characters)):
        for element in atoms:
            if characters[atom] == element:
                ma = atoms[element].mass
                elements.append(element)
                try:
                    if characters[atom + 1] in num:
                        ma = int(ma) * int(characters[atom + 1])
                        mol_of_elements[element] = int(characters[atom + 1])
                    else:
                        mol_of_elements[element] = 1
                except:
                    pass
                mm += int(ma)

    # returns a molecule object containing the processed data
    return molecule(
        molecular_formula=fm,
        molecule_mass=mm,
        molecules_amount=qm,
        atomos=elements,
        mol_of_elements=mol_of_elements
    )
