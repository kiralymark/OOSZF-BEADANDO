class Berles():

    def __init__(self, auto, nap):

        self.auto = auto
        self.nap = nap

    def get_berles_informacio(self):

        return f"A kibérelt autó: {self.auto.rendszam}, a bérlés dátuma: {self.nap}, a bérlés ára egy napra: {self.auto.berleti_dij} Ft"

