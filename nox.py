from atoms import atoms


def nox(mols):
    if len(mols) == 1:
        return 0
    else:
        for i in mols:
            print(f"{i} = {mols[i]}")

# HClO - ácido perclórico - H * o Cl o * O
# HClO2 - ácido clórico
# HClO3 - ácido cloroso
# HClO4 - ácido hipocloroso
