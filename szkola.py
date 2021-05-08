COMMANDS = ("wychowawca", "nauczyciel", "uczen", "end", "a")

clas_w = []
list_wychowawca = {}
list_nauczyciel = {}
list_uczen = {}
list_clas = []

while True:
    print("1) wychowawca\n2) nauczyciel\n3) uczen\n4) end")
    commands = input()
    if commands in COMMANDS:
        while True:
            if commands == "uczen":
                uczen = input("Podaj imie: ")
                clasa = input("Nazwa klasy: ")

                if uczen in list_uczen:
                    list_uczen[uczen] += clasa
                else:
                    list_uczen[uczen] = clasa
                print(list_uczen)

                if not uczen:
                    break

            if commands == "nauczyciel":
                nauczyciel = input("Podaj imie: ")
                przedmiot = input("Nazwa przedmiotu: ")
                if nauczyciel in list_nauczyciel:
                    list_nauczyciel[nauczyciel] += przedmiot
                else:
                    list_nauczyciel[nauczyciel] = przedmiot
                print(list_nauczyciel)
                while True:
                    clasa_n = input("Nazwa klasy: ")
                    if not clasa_n:
                        break

                    if clasa_n in list_clas:
                        list_clas += clasa_n
                    else:
                        list_clas = clasa_n

                    print(list_nauczyciel)
                    print(list_clas)

            if commands == "wychowawca":
                wychowawca = input("Podaj imie: ")
                clasa_w = (input("Nazwa klasy: "))
                clas_w.append((clasa_w))
                if wychowawca in list_wychowawca:
                    list_wychowawca[wychowawca] += clas_w
                else:
                    list_wychowawca[wychowawca] = clas_w
            print(list_wychowawca)

        if commands == "end":
            break
