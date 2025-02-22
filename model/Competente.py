import random

from model.CompetenteLingvistice import CompetenteLingvistice


class Competente:
    def __init__(self):
        self.__romana = self.generare_calificativ()
        self.__digitale = self.generare_calificativ()
        self.__lb_materna = self.generare_calificativ()
        self.__com_lingvistice = CompetenteLingvistice()
    def generare_calificativ(self):
        calificative = ["A1", "A2", "B1", "B2"]
        index = random.randint(1, 3)
        calificativ = calificative[index]
        return calificativ

    def get_romana(self):
        return self.__romana

    def get_digitale(self):
        return self.__digitale

    def get_lb_materna(self):
        return self.__lb_materna

    def get_com_lingvistice(self):
        return self.__com_lingvistice