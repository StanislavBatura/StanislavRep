print("Wpisz: ")
print(" 1)saldo\n2) sell\n3) buy\n4) end\n5) magazyn")

COMMANDS = ("saldo", "sell", "buy", "end", "magazyn")

summ_saldo = 1000
lista_operac = []
lista_magazyn = {}
while True:
    command = input()
    if command in COMMANDS:

        if command == "saldo":
            print(summ_saldo)

        if command == "buy":
            a = input("Podaj nazwe: ")
            b = int(input("Podaj iloszc: "))
            c = int(input("Podaj cene: "))
            summ_saldo = summ_saldo - c * b
            if a in lista_magazyn:
                lista_magazyn[a] += b
            else:
                lista_magazyn[a] = b
            lista_operac.append(f"buy: {a}, {b} szt, {c} zl")
        print(lista_magazyn)
        print(summ_saldo)
        print(lista_operac)
        if command == "sell":
            a = input("Podaj nazwe: ")
            b = int(input("Podaj iloszc: "))
            c = int(input("Podaj cene: "))

            summ_saldo = summ_saldo + c * b
            if a in lista_magazyn:
                lista_magazyn[a] -= b
            else:
                lista_magazyn[a] = b
            lista_operac.append(f"sell: {a}, {b} szt, {c} zl")

        print(lista_magazyn)
        print(summ_saldo)

        if command == "end":
            break
        if command == "magazyn":
            print(lista_magazyn)
    else:
        print("BLĄD")
        print("1) saldo\n2) sell\n3) buy\n4) end")
        continue