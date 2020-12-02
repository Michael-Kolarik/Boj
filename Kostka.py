class Kostka:  # Tahle třída jen definuje házení kostkou
    def __init__(self, pocet_sten):
        self.__pocet_sten = pocet_sten

    def hod(self):
        import random as _random
        if self.__pocet_sten > 0:
            vysledek = _random.randint(1, self.__pocet_sten)
        else:
            vysledek = 0
        return vysledek
    def vyhoda(self):
        prvnihod = self.hod()
        druhyhod = self.hod()
        if druhyhod > prvnihod:
            vystup = druhyhod
        else:
            vystup = prvnihod
        return vystup
    def nevyhoda(self):
        prvnihod = self.hod()
        druhyhod = self.hod()
        if druhyhod < prvnihod:
            vystup = druhyhod
        else:
            vystup = prvnihod
        return vystup
    def vyhodnoceni(self, vyhoda):
        if vyhoda == -1:
            hod = self.vyhoda()
        elif vyhoda == 1:
            hod = self.nevyhoda()
        else:
            hod = self.hod()
        return hod