import random
import json
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

    def __eq__(self, other):
        if other == None:
            return False
        if not isinstance(other, Student):
            return False
        c1 = self.get_numeFamilie() == other.get_numeFamilie()
        c2 = self.get_prenume() == other.get_prenume()
        c3 = self.get_data_nastere() == other.get_data_nastere()
        return c1 and c2 and c3

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

    def get_data_inmatriculare(self):
        return self.__data_inmatriculare

    #sa tin cont de pozele cu B si F
    def citire_cai_fisier(self, file):
        f = open(file, "r", encoding="utf-8")
        if f == None:
            raise Exception("Nu s-a deschis fisierul")
        cai = []
        for line in f:
            cai.append(line.strip())
        nr_poze_baieti = 0
        nr_poze_fete = 0
        for c in cai:
            if c[len(c) - 6] == 'B':
                nr_poze_baieti += 1
            elif c[len(c) - 6] == 'F':
                nr_poze_fete += 1
        cale = ""
        if self.get_sex() == 'M':
            rand_b = random.randint(1, nr_poze_baieti)
            cale = "D:\\PYTHON\\Generare_Studenti_Local\\imagini\\B" + str(rand_b) + ".jpg"
            return cale
        elif self.get_sex() == 'F':
            rand_f = random.randint(1, nr_poze_fete)
            cale = "D:\\PYTHON\\Generare_Studenti_Local\\imagini\\F" + str(rand_f) + ".jpg"
            return cale
        return "Cale inexistenta"

    def __repr__(self):
        persoana_info = super().__repr__()
        return f"{persoana_info}, Numar matricol: {self.__nr_matricol}, Data inmatriculare: {self.__data_inmatriculare}"

    def prepare(self):
        x = {
            "nume": self.get_numeFamilie(),
            "prenume": self.get_prenume(),
            "data_nastere":{
                "zi": self.get_data_nastere().day,
                "luna": self.get_data_nastere().month,
                "an": self.get_data_nastere().year
            },
            "sex": self.get_sex(),
            "varsta": self.get_varsta(),
            "data_inmatriculare":{
                "zi": self.__data_inmatriculare.day,
                "luna": self.__data_inmatriculare.month,
                "an": self.__data_inmatriculare.year
            },
            "nr_matricol": self.__nr_matricol,
            "cale_poza": self.__cale_poze
        }
        j = json.dumps(x)
        return j

student = Student('M', 23, date(2024, 2, 1))
student2 = Student('M', 21, date(2024, 2, 3))
student.prepare()
student2.prepare()