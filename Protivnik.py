
class Protivnik:
    def __init__(self, zivoty, obranne_cislo, kostka):
        self.__zivoty = zivoty
        self.__kostka = kostka
        self.__obranne_cislo = obranne_cislo
        self.__vyhoda_obrana = 0
        self.__vyhoda_utok = 0
    @property
    def vyhoda_obrana(self):
        return self.__vyhoda_obrana
    @property
    def vyhoda_utok(self):
        return self.__vyhoda_utok
    @property
    def zivoty (self):
        return self.__zivoty
    @property
    def obranne_cislo (self):
        return self.__obranne_cislo
    def prijmi_zraneni (self, zraneni):
        self.__zivoty = self.__zivoty - zraneni
        if self.__zivoty <= 0:
            self.__zivoty = 0
            print("Protivník umírá")
