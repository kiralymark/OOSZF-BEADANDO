from Autokolcsonzo import Autokolcsonzo
from Berles import Berles
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto

class Program:
    def __init__(self):

        self.kolcsonzo = Autokolcsonzo("Heisenberg Autókölcsönző")

        self.kolcsonzo.autok_hozzaadasa(Szemelyauto("FFGD-9823", "2018 Ford Focus ST-Line X", 5000, 4, 1300))
        self.kolcsonzo.autok_hozzaadasa(Szemelyauto("TPKL-6770", "2016 Toyota Prius XW50", 4000, 4, 1700))
        self.kolcsonzo.autok_hozzaadasa(Teherauto("MTZP-4467", "2021 MAN TGE 3.140", 16000, 2500))

        self.kolcsonzo.berlesek_lista.append(Berles(self.kolcsonzo.autok_lista[0], "2024-08-01"))
        self.kolcsonzo.berlesek_lista.append(Berles(self.kolcsonzo.autok_lista[1], "2024-08-12"))
        self.kolcsonzo.berlesek_lista.append(Berles(self.kolcsonzo.autok_lista[2], "2024-08-23"))
        self.kolcsonzo.berlesek_lista.append(Berles(self.kolcsonzo.autok_lista[0], "2024-09-04"))

    def felhasznaloi_menu(self):
        print("Heisenberg Autókölcsönző Rendszere")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")

        while True:

            valasz = input("Válasz a fenti menüpontok közül: ")

            if valasz == "1":
                rendszam = input("Add meg az autó rendszámát, amit ki szeretnél bérelni: ")
                datum = input("Add meg a bérlés napját (YYYY-MM-DD): ")
                eredmeny = self.kolcsonzo.auto_berlese(rendszam, datum)
                print(eredmeny)

            elif valasz == "2":
                rendszam = input("Add meg az autó rendszámát, amit szeretnél lemondani: ")
                datum = input("Add meg a lemondás napját (YYYY-MM-DD): ")
                eredmeny = self.kolcsonzo.berles_lemondasa(rendszam, datum)
                print(eredmeny)

            elif valasz == "3":
                print(self.kolcsonzo.berlesek_listazasa())

            elif valasz == "4":
                print("Kilépés...")
                break

            else:
                print("Érvénytelen menüpont, próbáld újra.")


# A Program futtatása
program_indit = Program()
program_indit.felhasznaloi_menu()

