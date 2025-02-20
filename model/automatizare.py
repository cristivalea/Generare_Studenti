import random


class Persoana:
    def __init__(self, sex, varsta):
        if varsta < 18:
            raise Exception("Varsta invalida")
        nrNumeFamilie = random.randint(1,38625)
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
    def __repr__(self):
        return self.__numeFamilie + " " + self.__prenume

p1 = Persoana('M', 22)
p2= Persoana('F', 19)
print(p1)
print(p2)