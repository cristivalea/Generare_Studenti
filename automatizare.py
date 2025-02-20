import random


class Persoana:
    def __init__(self):
        nrNumeFamilie = random.randint(1,38625)
        nume = []
        file = open("NumeFamilieF.txt","r",encoding= "utf-8")
        if file == None:
            raise Exception("Fisierul nu a putut fi deschis")
        else:
            for linie in file:
                nume.append(linie)

        self.__numeFamilie = nume[nrNumeFamilie]
        nrSex = random.randint(1,2)

    def __repr__(self):
        return self.__numeFamilie

p1 = Persoana()
print(p1)