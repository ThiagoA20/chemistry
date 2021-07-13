from mass import molecular_mass
from nomenclature import name
from nox import nox
from valence_layer import layers
from atoms import atoms
import time

if __name__ == "__main__":
    while True:
        print(f"---------- Operation ----------\n\n1 - Molecular Mass\n2 - Nomenclature\n3 - Oxidation Number\n4 - "
              f"Atom valence\n5 - ionic_dissociation\n6 - ...")
        number = str(input("\nType a number: "))
        if number == '1':
            molecule = str(input("Type a molecule: "))
            molecule = molecular_mass(molecule)
            print(f"\nMolecular mass: {molecule.mm}g/mol")
            print(f"Amount of molecules: {molecule.qm}")
            if molecule.mm != molecule.mc:
                print(f"Calculated mass: {molecule.mc}")
            print(f"Atoms in molecule: {molecule.atoms}")
        elif number == '2':
            molecule = str(input("Type a molecule: "))
            molecule = molecular_mass(molecule)
            print(name(molecule, nox(molecule.mol_of_elements)).nomenclature)
        elif number == '3':
            print("Working on! :)")
            """molecule = str(input("Type a molecule: "))
            molecule = molecular_mass(molecule)
            nox(molecule.mol_of_elements)"""
        elif number == '4':
            atomic_number = str(input("Type the acronym of an atom: "))
            atomic_number = atoms[atomic_number].num
            print(layers(atomic_number))
        elif number == '5':
            pass
        else:
            print("Invalid Number!")

        time.sleep(5)
        c = str(input("\nContinue? (Y/N): "))
        if c.lower() == "y":
            pass
        elif c.lower() == "n":
            break
        else:
            pass
