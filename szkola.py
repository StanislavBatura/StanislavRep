lista_nauczycieli = {}
lista_wychowawcy = {}
lista_uczni = {}
lista_klas = []
lista_klasy_wychowawcy = {}

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
            lista_klas.append(klasa)

class Uczen:

    def __init__(self):
        self.name = ""
        self.klasy = ""

    def get_data(self):
        return

    def input_data(self):
        self.uczen = input("Podaj imie: ")
        self.klasy = input("Nazwa klasy: ")
        if self.klasy not in lista_uczni:
            lista_uczni[self.klasy] = []
        lista_uczni[self.klasy].append(self.uczen)

class Wychowawca:

    def __init__(self):
        self.name = ""
        self.klasy = ""

    def get_data(self):
        return

    def input_data(self):
        self.wychowawca = input("Podaj Imie i Nazwisko: ")
        while True:
            self.klasy = input("Podaj klasę: ")
            if not self.klasy:
                break
            if self.klasy not in lista_wychowawcy:
                lista_wychowawcy[self.klasy] = []
            lista_wychowawcy[self.klasy].append(self.wychowawca)


COMMANDS = ("wychowawca", "nauczyciel", "uczen", "end", "nazwa klasy", "name uczen", "nazwa wychowawcy")

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
        lista_uczni[u.name] = u.get_data()
        print(lista_uczni)

    if command == "wychowawca":

        w = Wychowawca()
        w.input_data()
        lista_wychowawcy[w.name] = w.get_data()
        print(lista_wychowawcy)

    if command == "nazwa klasy":
        klasa = input("Podaj nazwe klasy: ")
        for nazwa_klasy, wychowawcy in lista_wychowawcy.items():
            if klasa == nazwa_klasy:
                print(wychowawcy)

    if command == "nazwa wychowawcy":
        wych = input("Podaj imie wychowawcy: ")
        for nazwa_klasy, wychowawcy in lista_wychowawcy.items():
            if wychowawcy:
                if wych in wychowawcy:
                    print(nazwa_klasy)
                    for k, f in lista_uczni.items():
                        if k == nazwa_klasy:
                            print(k)