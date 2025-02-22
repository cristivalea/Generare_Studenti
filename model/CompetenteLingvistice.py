import random


class CompetenteLingvistice:
    def __init__(self):
        self.__audiat = self.generare_calificativ()
        self.__citit = self.generare_calificativ()
        self.__scris = self.generare_calificativ()
        self.__oral = self.generare_calificativ()
        self.__interactiune_orala = self.generare_calificativ()

    def generare_calificativ(self):
        calificative = ["A1", "A2", "B1", "B2"]
        index = random.randint(1, 3)
        calificativ = calificative[index]
        return calificativ

    def __repr__(self):
        return self.__audiat + " " + self.__citit + " " + self.__scris + " " + self.__oral + " " + self.__interactiune_orala

    def get_audiat(self):
        return self.__audiat

    def get_citit(self):
        return self.__citit

    def get_scris(self):
        return self.__scris

    def get_orala(self):
        return self.__oral

    def get_interactiune_orala(self):
        return self.__interactiune_orala


# comp = CompetenteLingvistice()
# print(comp)