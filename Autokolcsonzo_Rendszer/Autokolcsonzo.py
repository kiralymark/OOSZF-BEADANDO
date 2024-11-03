from Berles import Berles

class Autokolcsonzo():

    def __init__(self, kolcsonzo_nev):

        self.kolcsonzo_nev = kolcsonzo_nev
        self.autok_lista = []
        self.berlesek_lista = []

    def autok_hozzaadasa(self, auto):

        self.autok_lista.append(auto)

    def auto_berlese(self, rendszam, nap):

        for auto in self.autok_lista:
            if auto.rendszam == rendszam:
                for berles in self.berlesek_lista:
                    if berles.auto.rendszam == rendszam and berles.nap == nap:
                        return "Az autó már ki van bérelve erre a napra."

                uj_berles = Berles(auto, nap)
                self.berlesek_lista.append(uj_berles)

                return f"A bérlés sikeres. A bérlés ára: {auto.berleti_dij} Ft lesz."

        return "Nem bérelhető ezzel a rendszámmal autó."
                
    def berles_lemondasa(self, rendszam, nap):

        for berles in self.berlesek_lista:
            if berles.auto.rendszam == rendszam and berles.nap == nap:
                self.berlesek_lista.remove(berles)
                return "A bérlés le van mondva."

        return "Nincs ilyen bérlés."

    def berlesek_listazasa(self):

        if not self.berlesek_lista:
            return "Nincsenek jelenleg bérlések."

        return "\n".join(
            f"A kibérelt autó: {berles.auto.rendszam}, a bérlés dátuma: {berles.nap}, a bérlés ára egy napra: {berles.auto.berleti_dij} Ft."
            for berles in self.berlesek_lista
        )
