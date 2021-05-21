lista_nauczycieli = {}
lista_wychowawcy = {}
lista_uczni = {}

class Nauczyciel:

    def __init__(self):
        self.name = ""
        self.przedmiot = ""
        self.klasy = []

    def get_data(self):
        return {"przedmiot": self.przedmiot, "klasy": self.klasy}

    def input_data(self):
        self.name = input("Podaj Imie i Nazwisko: ")
        self.przedmiot = input("Podaj przemiot: ")

        while True:
            klasa = input("Podaj klasę: ")
            if not klasa:
                break
            self.klasy.append(klasa)

class Uczen:

    def __init__(self):
        self.name = ""
        self.klasa = ""

    def input_data(self):
        self.uczen = input("Podaj imie: ")
        self.klasa = input("Nazwa klasy: ")
        if self.klasa not in lista_uczni:
            lista_uczni[self.klasa] = [self.uczen]
        else:
            lista_uczni[self.klasa].append(self.uczen)

class Wychowawca:

    def __init__(self):
        self.name = ""
        self.klasy = []

    def input_data(self):
        self.name = input("Podaj Imie i Nazwisko: ")
        while True:
            klasa = input("Podaj klasę: ")
            if not klasa:
                break
            self.klasy.append(klasa)
        lista_wychowawcy[self.name] = self.klasy
        #if self.klasa not in lista_wychowawcy:
        #    lista_wychowawcy[self.klasa] = [self.wychowawca] # TUTAJ DODALEM BO BYŁA PUSTA LISTA
        #lista_wychowawcy[self.klasa].append(self.wychowawca)


COMMANDS = ("wychowawca", "nauczyciel", "uczen", "end", "nazwa klasy", "name uczen", "nazwa wychowawcy",
            "nazwa nauczyciela", "nazwa ucznia")

while True:
    command = input("Podaj komendę: ")

    if not command:
        break
    if command not in COMMANDS:
        continue
    if command == "end":
        break

    if command == "nauczyciel":
        n = Nauczyciel()
        n.input_data()
        lista_nauczycieli[n.name] = n.get_data()
        print(lista_nauczycieli)

    if command == "uczen":
        u = Uczen()
        u.input_data()
        print(lista_uczni)

    if command == "wychowawca":
        w = Wychowawca()
        w.input_data()
        print(lista_wychowawcy)

    if command == "nazwa klasy":
        klasa = input("Podaj nazwe klasy: ")
        for nazwa_klasy, wychowawcy in lista_wychowawcy.items():
            if klasa == nazwa_klasy:
                print(f'Wycowawcy klasy {klasa} to: {wychowawcy}')

    if command == "nazwa wychowawcy":
        wych = input("Podaj imie wychowawcy: ")
        if wych in lista_wychowawcy.keys():
            print(f'Klasy wychowacy {wych} to: {lista_wychowawcy[wych]}')
            for klasa, uczniowie in lista_uczni.items():
                if klasa in lista_wychowawcy[wych]:
                    print(f'Wychowawca {wych} uczy: {uczniowie} z klasy {klasa}')
        else:
            print(f"Brak wychowacy {wych} w bazie!")

    if command == "nazwa nauczyciela":
        naucz = input("Podaj imie nauczyciela: ")
        if naucz in lista_nauczycieli.keys():
            #print(f'Klasy wychowacy {naucz} to: {lista_nauczycieli[naucz]}')
            #print(lista_nauczycieli[naucz])
            for key, klasy in lista_nauczycieli.items():
                print(klasy)
                for i, klas in klasy.items():

                    print(klas)
                    for a, b in lista_wychowawcy.items():
                        print(b)
                        if b in lista_wychowawcy.items():
                            print(lista_wychowawcy)
                            #print(lista_wychowawcy[b])
                    #print(f'Wychowawca {wych} uczy
                    # : {uczniowie} z klasy {klasa}')

    if command == "nazwa ucznia":
        ucz = input("Podaj imie ucznia: ")
        if ucz in lista_uczni.items():
            #print(f'Klasy wychowacy {naucz} to: {lista_nauczycieli[naucz]}')
            print(lista_uczni[ucz])
            for key, klasy in ucz.items():
                print(key)  
                print(klasy)

               # for i, klas in klasy.items():
               #     if klas in lista_wychowawcy[wych]:
               #         print(lista_wychowawcy[wych])