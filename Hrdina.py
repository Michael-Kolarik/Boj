from Kostka import Kostka
class Hrdina:
    def __init__(self, zivoty):
        self.__zivoty = zivoty
        self.__kostka = Kostka(20)
        self.__obranne_cislo = 17
        self.__utocne_cislo = 6
        self.__sila = 3
        self.__obratnost = 3
        self.__vyhoda_obrana = 0
        self.__vyhoda_utok = 0
        self.__zraneni = Kostka(10)
        self.__manevr = False
        self.__druhy_dech = 1
        self.__akcni_vlna = 1
        self._kostky_manevru = 4

    @property
    def vyhoda_obrana(self):
        return self.__vyhoda_obrana

    @property
    def sila(self):
        return self.__sila
    @property
    def obratnost(self):
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
            print("umíráš")
    def utok(self, cil):
        vyhody = self.vyhoda_utok + cil.vyhoda_obrana
        hod_kostkou = self.__kostka.vyhodnoceni(vyhody)
        print("Chceš použít riskantní útok? A - Ano, N - Ne")
        riskantni_utok = input()
        if riskantni_utok == "A":
            bonus_k_utoku = 1
            bonus_ke_zraneni = 13
        else:
            bonus_k_utoku = 6
            bonus_ke_zraneni = 3
        if hod_kostkou == 20:
            print("Tvůj bojovník zasáhl.")
            zraneni = self.__zraneni.hod() + self.__zraneni.hod() + bonus_ke_zraneni
            cil.prijmi_zraneni(zraneni)
            self.__manevr = True
        elif hod_kostkou + bonus_k_utoku >= cil.obranne_cislo:
            print("Tvůj bojovník zasáhl.")
            zraneni = self.__zraneni.hod() + bonus_ke_zraneni
            cil.prijmi_zraneni(zraneni)
            if hod_kostkou + bonus_k_utoku >= cil.obranne_cislo + 5:
                self.__manevr = True
        else:
            print("Tvůj bojovník minul.")

    def akce(self):
        print("Rozhodni, co bojovník udělá.")
        print("Bude útočit - stiskni U")
        print("Bude se bránit - stiskni O")
        volba = input()








