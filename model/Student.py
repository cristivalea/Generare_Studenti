import random
from datetime import date
from datetime import timedelta

from model.Persoana import Persoana


class Student(Persoana):
    def __init__(self, sex, varsta, data_inmatriculare):
        super().__init__(sex, varsta)
        self.__data_inmatriculare = data_inmatriculare
        self.__nr_matricol = self.generare_numar_matricol()
        self.__cale_poze = self.citire_cai_fisier("cai_imagini.txt")
        #print(self.__cale_poze)


    def generare_numar_matricol(self):
        nr_matricol = "CTI0"
        data_curenta = self.__data_inmatriculare
        an_curent = data_curenta.year
        nr_matricol += str(an_curent % 100)
        numar = random.randint(100, 1000)
        coduri_nr_matricole = []
        if numar not in coduri_nr_matricole:
            coduri_nr_matricole.append(numar)
            nr_matricol += str(numar)
        else:
            self.generare_numar_matricol()
        return nr_matricol
    def get_nr_matricol(self):
        return self.__nr_matricol

    def generare_data_inmatriculare(self, data_start, data_end):
        diferenta_zile = (data_end - data_start).days
        zile_aleatoare = random.randint(0, diferenta_zile)
        data_inmatriculare = data_start + timedelta(days=zile_aleatoare)
        return data_inmatriculare

    def get_data_inmatriculare(self):
        return self.__data_inmatriculare

    #sa tin cont de pozele cu B si F
    def citire_cai_fisier(self, file):
        f = open(file, "r", encoding="utf-8")
        if f == None:
            raise Exception("Nu s-a deschis fisierul")
        cai = []
        for line in f:
            cai.append(line)
        return cai

    def __repr__(self):
        persoana_info = super().__repr__()
        return f"{persoana_info}, Numar matricol: {self.__nr_matricol}, Data inmatriculare: {self.__data_inmatriculare}"


student1 = Student('M', 20, date.today())
print(student1)