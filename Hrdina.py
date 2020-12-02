
class Hrdina:
    def __init__(self, zivoty, kostka):
        self.__zivoty = zivoty
        self.__kostka = kostka
        self.__obranne_cislo = 17

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
            print("umíráš")
