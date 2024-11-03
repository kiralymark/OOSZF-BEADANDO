from Auto import Auto

class Teherauto(Auto):

    def __init__(self, rendszam, auto_tipus, berleti_dij, hasznos_terhelhetoseg):

        super().__init__(rendszam, auto_tipus, berleti_dij)
        self.hasznos_terhelhetoseg = hasznos_terhelhetoseg

    def get_auto_informacio(self):

        return f"A Teherautó rendszáma: {self.rendszam}, típusa: {self.auto_tipus}, a hasznos terhelhetősége: {self.hasznos_terhelhetoseg} liter, a bérleti díja: {self.berleti_dij} Ft/nap"

