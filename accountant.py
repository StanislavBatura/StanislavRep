print("Wpisz: ")
print(" 1) saldo\n2) sell\n3) buy\n4) end")

COMMANDS = ("saldo", "sell", "buy", "end")
summ_saldo = 1000
lista_operac = {}
lista_magazyn = {"rower": 0, "truskawka": 0}
d = 0
f = 0
while True:
    command = input()
    if command in COMMANDS:

        if command == "saldo":
            #print("Kwota: ")
            #kwota = input()
            #lista_saldo.append(kwota)
            print(summ_saldo)

        if command == "buy":
            a = input("Podaj nazwe: ")
            b = int(input("Podaj iloszc: "))
            c = int(input("Podaj cene: "))

            if a == "rower":
                d = d + b
                lista_magazyn["rower"] = d
                summ_saldo = summ_saldo - c*b
                if d < 0:
                    break
            if a == "truskawka":
                f = f + b
                lista_magazyn["truskawka"] = f
                summ_saldo = summ_saldo - c*b
                if f < 0:
                    break
        print(lista_magazyn)
        print(summ_saldo)

        if command == "sell":
            a = input("Podaj nazwe: ")
            b = int(input("Podaj iloszc: "))
            c = int(input("Podaj cene: "))

            if a == "rower":
                d = d - b
                lista_magazyn["rower"] = d
                summ_saldo = summ_saldo + c * b
            if a == "truskawka":
                f = f - b
                lista_magazyn["truskawka"] = f
                summ_saldo = summ_saldo + c * b
        print(lista_magazyn)
        print(summ_saldo)

        if command == "end":
            break
