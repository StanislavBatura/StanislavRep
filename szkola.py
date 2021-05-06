COMMANDS = ("wychowawca", "nauczyciel", "uczen", "end")


list_wychowawca = {}
list_nauczyciel = {}
list_uczen = {}
list_clas = {}
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

    while True:
        commands = input()
        if commands in COMMANDS:
            if commands == "nauczyciel":
                nauczyciel = input("Podaj imie: ")
                przedmiot = input("Nazwa przedmiotu: ")
                clasa_n = input("Nazwa klasy: ")
                if not clasa_n:
                    break
                print(list_clas)

                if clasa_n in list_clas:
                    list_clas += clasa_n
                else:
                    list_clas = clasa_n


                print(list_clas)
       # else:
        #    list_nauczyciel[nauczyciel] = przedmiot
        print(list_nauczyciel)

        if commands == "wychowawca":
            pass

        if commands == "end":
            break