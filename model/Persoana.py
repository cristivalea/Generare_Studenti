import random

import dateutil.utils
from datetime import date

class Persoana:
    def __init__(self, sex, varsta):
        if varsta < 18:
            raise Exception("Varsta invalida")
        nrNumeFamilie = random.randint(1,38265)
        nume = []
        file = open("NumeFamilieF.txt", "r", encoding="utf-8")
        if file == None:
            raise Exception("Fisierul nu a putut fi deschis")
        else:
            for linie in file:
                nume.append(linie)

        self.__numeFamilie = nume[nrNumeFamilie]
        nr_prenume = random.randint(1, 5)
        pren = []
        if sex == 'M':
            file = open("PrenumeBaieti.txt", "r", encoding="utf-8")
        elif sex == 'F':
            file = open("PrenumeFete.txt", "r", encoding="utf-8")
        if file == None:
            raise Exception("fisierul de prenume nu a putut fi deschis")
        else:
            for linie in file:
                pren.append(linie)
        print(nr_prenume)
        self.__prenume = ""
        for i in range(nr_prenume):
            index_prenume = random.randint(0, len(pren)-1)
            self.__prenume += pren[index_prenume]

        data_curenta = dateutil.utils.today()
        an = data_curenta.year
        an_nastere = an - varsta
        luna_nastere = random.randint(1, 12)
        zi_nastere = 0
        if luna_nastere in [1, 3, 5, 7, 8, 10, 12]:
            zi_nastere = random.randint(1, 31)
        elif luna_nastere in [4, 6, 9, 11]:
            zi_nastere = random.randint(1, 30)
        elif luna_nastere == 2 and an_nastere % 4 == 0:
            zi_nastere = random.randint(1, 29)
        elif luna_nastere == 2:
            zi_nastere = random.randint(1, 28)
        data_nastere = date(an_nastere, luna_nastere, zi_nastere)
        self.__data_nastere = data_nastere
        self.__varsta = varsta
        self.__sex = sex

    def __repr__(self):
        return self.__numeFamilie + " " + self.__prenume

    def get_numeFamilie(self):
        return self.__numeFamilie

    def get_prenume(self):
        return self.__prenume

    def get_data_nastere(self):
        return self.__data_nastere

    def get_varsta(self):
        return self.__varsta

    def get_sex(self):
        return self.__sex

# p1 = Persoana('M', 22)
# p2= Persoana('F', 19)
# print(p1)
# print(p2)

