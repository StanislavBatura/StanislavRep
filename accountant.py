class Saldo:

    def __init__(self):
        self.saldo = ""
        self.komentaz = ""
        self.lista_operac = []

    def add_saldo(self):
        self.saldo = int(input("Podaj kwote: "))
        self.komentaz = input("komentarz: ")
        self.lista_operac.append(f"{self.saldo},{self.komentaz}")

    def saldo_show(self):
        print(self.saldo)

    def read_saldo(self):
        with open("saldo.txt", "r") as file:
            summa_saldo = 0
            for line in file.readlines():
                saldo = line.split(",")[0]
                komentaz = line.split(",")[1].split("\n")[0]
                summa_saldo += int(saldo)
            print(summa_saldo)
            self.saldo = summa_saldo

    def save(self):
        with open("saldo.txt", "a") as file:
            for sell in self.lista_operac:
                file.write(str(sell.split(",")[0]) + "," + str(sell.split(",")[1]) + "\n")
        print(self.lista_operac)


class Magazyn:

    def __init__(self):
        self.summa_saldo = 0
        self.lista_magazyn = {}
        self.lista_operac = []

    def read_saldo(self):
        with open("saldo.txt", "r") as file:
            summa_saldo = 0
            for line in file.readlines():
                saldo = line.split(",")[0]
                komentaz = line.split(",")[1].split("\n")[0]
                summa_saldo += int(saldo)
            print(summa_saldo)
            self.summa_saldo = summa_saldo

    def add_sell(self):

        self.towar_sell = input("Podaj nazwe: ")
        self.iloszc_sell = int(input("Podaj iloszc: "))
        self.cena_sell = int(input("Podaj cene: "))
        if int(self.lista_magazyn[self.towar_sell]) - int(self.iloszc_sell) < 0:
            print(f"w magaz masz {self.lista_magazyn[self.towar_sell]}, a chcesz spszedac {self.iloszc_sell}")

        self.summa_saldo = self.summa_saldo + self.cena_sell * self.iloszc_sell
        if self.towar_sell in self.lista_magazyn:
            self.lista_magazyn[self.towar_sell] -= self.iloszc_sell   #str int
        else:
            self.lista_magazyn[self.towar_sell] = self.iloszc_sell
        self.lista_operac.append(f"sell: {self.towar_sell}, {self.iloszc_sell} szt, {self.cena_sell} zl")

    def add_buy(self):

        self.towar = str(input("Podaj nazwe: "))
        self.sztuki = int(input("Podaj iloszc: "))
        self.cena = int(input("Podaj cene: "))
        self.summa_saldo = int(self.summa_saldo) - int(self.sztuki) * int(self.cena)
        if self.towar in self.lista_magazyn:
            self.lista_magazyn[self.towar] += self.sztuki #str int
        else:
            self.lista_magazyn[self.towar] = self.sztuki
        self.lista_operac.append(f"buy: {self.towar}, {self.sztuki} szt, {self.cena} zl")

        print(self.lista_magazyn)
        print(self.summa_saldo)

    def magazyn_show(self):
        print(self.lista_magazyn)

    def save(self):
        with open("magazyn.txt", "w") as file:
            for sell, iloszc in self.lista_magazyn.items():
                print(sell)
                print(iloszc)
                file.write(str(sell) + "," + str(iloszc) + "\n")
                print(sell)
        print(self.lista_magazyn)


    def read_magazyn(self):
        with open("magazyn.txt", "r") as file:
            for line in file.readlines():
                towar = line.split("\n")[0].split(",")[0]
                iloszc = line.split("\n")[0].split(",")[1]
                self.lista_magazyn[towar] = iloszc


print("Wpisz: ")
print(" 1)saldo\n2) sell\n3) buy\n4) end\n5) magazyn")

COMMANDS = ("saldo", "sell", "buy", "end", "magazyn")


lista_magazyn = {}
konto = Saldo()
konto.read_saldo()

magazyn = Magazyn()
magazyn.read_saldo()
magazyn.read_magazyn()
while True:
    command = input()
    if command in COMMANDS:

        if command == "saldo":
            konto.add_saldo()

        if command == "buy":
            magazyn.add_buy()

        if command == "sell":
            magazyn.add_sell()
            """
            a = input("Podaj nazwe: ")
            b = int(input("Podaj iloszc: "))
            c = int(input("Podaj cene: "))
            if lista_magazyn[a] - b < 0:
                print(f"w magaz masz {lista_magazyn[a]}, a chcesz spszedac {b}")
                continue

            summ_saldo = summ_saldo + c * b
            if a in lista_magazyn:
                lista_magazyn[a] -= b
            else:
                lista_magazyn[a] = b
            #lista_operac.append(f"sell: {a}, {b} szt, {c} zl")
"""
        if command == "end":
            konto.save()
            magazyn.save()
            break
        if command == "magazyn":
            magazyn.magazyn_show()
    else:
        print("BLĄD")
        print("1) saldo\n2) sell\n3) buy\n4) end")
        continue
