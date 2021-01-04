from massa import massa_molecular
from nomenclatura import name
import time

if __name__ == "__main__":
    while True:
        print(f"---------- Operação ----------\n\n1 - Massa Molecular\n2 - Nomenclatura\n3 - ...")
        number = int(input("\nDigite um número: "))
        if number == 1:
            molecula = str(input("Digite uma molécula: "))
            molecula = massa_molecular(molecula)
            print(f"\nFórmula molecular: {molecula.fm}")
            print(f"Massa molecular por mol: {molecula.mm}g")
            print(f"Quantidade de moléculas: {molecula.qm}")
            if molecula.mm != molecula.mc:
                print(f"Massa calculada: {molecula.mc}")
            print(f"Átomos na molécula: {molecula.atomos}")
        elif number == 2:
            molecula = str(input("Digite uma molécula: "))
            molecula = massa_molecular(molecula)
            print(name(molecula).nomenclatura)

        time.sleep(5)
        c = str(input("\nDeseja continuar? (S/N): "))
        if c.lower() == "s":
            pass
        else:
            break
