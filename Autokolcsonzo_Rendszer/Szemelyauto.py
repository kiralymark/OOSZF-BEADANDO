from Auto import Auto

class Szemelyauto(Auto):

    def __init__(self, rendszam, auto_tipus, berleti_dij, ajtok_szama, hasznos_terhelhetoseg):

        super().__init__(rendszam, auto_tipus, berleti_dij)
        self.ajtok_szama = ajtok_szama
        self.hasznos_terhelhetoseg = hasznos_terhelhetoseg

    def get_auto_informacio(self):

        return f"A Személyautó rendszáma: {self.rendszam}, típusa: {self.auto_tipus}, az ajtók száma: {self.ajtok_szama} db, a hasznos terhelhetősége: {self.hasznos_terhelhetoseg} liter, a bérleti díja: {self.berleti_dij} Ft/nap"
