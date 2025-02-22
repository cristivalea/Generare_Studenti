import random

import dateutil.utils
from datetime import date

from model.Adresa import Adresa


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
                nume.append(linie.strip())

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
                pren.append(linie.strip())
        #print(nr_prenume)
        self.__prenume = []
        for i in range(nr_prenume):
            index_prenume = random.randint(0, len(pren)-1)
            self.__prenume.append(pren[index_prenume])

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
        self.__cnp = self.generare_cnp()
        self.__serie_buletin = self.generare_serie_buletin()
        self.__nr_buletin = self.generare_numar_buletin()
        self.__adresa = self.generare_adresa()
        self.__eliberare_buletin = self.generare_buletin_eliberat()
        self.__nume_tata = self.generare_nume_prenume_tata()
        self.__nume_mama = self.generare_nume_mama()

    def __repr__(self):
        string = self.__numeFamilie + " " + self.__prenume + " " + self.__cnp + " " + str(self.__data_nastere) + " "
        string += str(self.__varsta) + " " + self.__sex +  " " + self.__serie_buletin + " "
        string += str(self.__nr_buletin) + " " + self.__adresa.__repr__() + " " + self.__eliberare_buletin + " "
        string += self.__nume_tata + " " + self.__nume_mama
        return string

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

    def get_cnp(self):
        return self.__cnp

    def get_serie_buletin(self):
        return self.__serie_buletin

    def get_nr_buletin(self):
        return self.__nr_buletin

    def get_adresa(self):
        return self.__adresa

    def get_eliberare_buletin(self):
        return self.__eliberare_buletin

    def get_nume_tata(self):
        return self.__nume_tata

    def get_nume_mama(self):
        return self.__nume_mama

    def generare_cnp(self):
        #Prima cifra din cnp
        c1 = 0
        if self.__sex == 'M' and (self.__data_nastere.year >= 1900 and self.__data_nastere.year <= 1999):
            c1 = 1
        elif self.__sex == 'F' and (self.__data_nastere.year >= 1900 and self.__data_nastere.year <= 1999):
            c1 = 2
        elif self.__sex == 'M' and (self.__data_nastere.year >= 2000):
            c1 = 5
        elif self.__sex == 'F' and (self.__data_nastere.year >= 2000):
            c1 = 6
        else:
            c1 = random.randint(7, 9)

        #urmatoarele 6 cifre in functie de data nasterii
        an = self.__data_nastere.year % 100
        luna = self.__data_nastere.month
        zi = self.__data_nastere.day

        #urmatoarele 2 cifre - cod judet
        cod_judet = random.randint(1, 52)

        #urmatoarele 3 cifre - cod unic
        cod_unic = random.randint(100, 999)

        # Construim primele 12 cifre
        cnp_fara_control = f"{c1}{an:02}{luna:02}{zi:02}{cod_judet:02}{cod_unic}"

        # Calculăm cifra de control
        cifra_control = self.calculeaza_cifra_control(cnp_fara_control)

        # Returnăm CNP complet
        return cnp_fara_control + str(cifra_control)

    def calculeaza_cifra_control(self, cnp_fara_control):
        # Șirul de ponderi fix pentru calcul
        ponderi = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

        # Calculăm suma ponderată
        suma = sum(int(cnp_fara_control[i]) * ponderi[i] for i in range(12))

        # Cifra de control este restul împărțirii la 11
        cifra_control = suma % 11
        return 1 if cifra_control == 10 else cifra_control

    def generare_serie_buletin(self):
        coduri_judet = [
            "AB", "AR", "AG", "BC", "BH", "BN", "BR", "BT", "BV", "BZ",
            "CS", "CL", "CJ", "CT", "CV", "DB", "DJ", "GL", "GR", "GJ",
            "HR", "HD", "IL", "IS", "IF", "MM", "MH", "MS", "NT", "OT",
            "PH", "SM", "SJ", "SB", "SV", "TR", "TM", "TL", "VS", "VL", "VN",
            "B1", "B2", "B3", "B4", "B5", "B6"
        ]
        nr = random.randint(0, 47)
        serie_buletin = coduri_judet[nr - 1]
        return serie_buletin

    def generare_numar_buletin(self):
        nr_buletin = random.randint(100000, 999999)
        return nr_buletin

    def generare_adresa(self):
        orase_romania = [
            "București", "Cluj-Napoca", "Timișoara", "Iași", "Constanța", "Craiova", "Brașov", "Galați", "Ploiești",
            "Oradea",
            "Brăila", "Arad", "Pitești", "Sibiu", "Bacău", "Târgu Mureș", "Baia Mare", "Buzău", "Botoșani", "Satu Mare",
            "Râmnicu Vâlcea", "Drobeta-Turnu Severin", "Suceava", "Piatra Neamț", "Târgu Jiu", "Târgoviște", "Focșani",
            "Bistrița", "Tulcea", "Reșița", "Slatina", "Călărași", "Alba Iulia", "Giurgiu", "Deva", "Hunedoara",
            "Zalău",
            "Sfântu Gheorghe", "Bârlad", "Vaslui", "Roman", "Slobozia", "Turda", "Medgidia", "Alexandria", "Lugoj",
            "Petroșani", "Miercurea Ciuc", "Pașcani", "Sighetu Marmației", "Câmpina", "Blaj", "Tecuci", "Sighișoara"
        ]

        strazi_romania = [
            "Strada Mihai Eminescu", "Strada Victoriei", "Strada Ștefan cel Mare", "Strada Libertății",
            "Strada Avram Iancu", "Strada Griviței", "Strada Horea", "Strada Nicolae Bălcescu",
            "Strada Tudor Vladimirescu", "Strada 1 Decembrie 1918", "Strada Gheorghe Doja", "Strada Ion Creangă",
            "Strada Unirii", "Strada Calea Moșilor", "Strada Carol I", "Strada Eroilor", "Strada Mărășești",
            "Strada Cuza Vodă", "Strada Traian", "Strada Decebal", "Strada Basarabia", "Strada Dorobanților",
            "Strada Mihail Kogălniceanu", "Strada Transilvaniei", "Strada George Coșbuc", "Strada Independenței"
        ]

        indice_oras = random.randint(0, len(orase_romania) - 1)
        oras = orase_romania[indice_oras]
        indice_strada = random.randint(0, len(strazi_romania) - 1)
        strada = strazi_romania[indice_strada]
        numar = random.randint(1, 40)
        bloc = random.randint(0, 20)
        apartament = 0
        if bloc != 0:
            apartament = random.randint(1, 36)
        adresa = Adresa(oras, strada, numar, bloc, apartament)
        return adresa

    def generare_buletin_eliberat(self):
        judete_romania = [
            "Alba", "Arad", "Argeș", "Bacău", "Bihor", "Bistrița-Năsăud", "Botoșani", "Brașov", "Brăila", "Buzău",
            "Caraș-Severin", "Călărași", "Cluj", "Constanța", "Covasna", "Dâmbovița", "Dolj", "Galați", "Giurgiu",
            "Gorj",
            "Harghita", "Hunedoara", "Ialomița", "Iași", "Ilfov", "Maramureș", "Mehedinți", "Mureș", "Neamț", "Olt",
            "Prahova", "Satu Mare", "Sălaj", "Sibiu", "Suceava", "Teleorman", "Timiș", "Tulcea", "Vaslui", "Vâlcea",
            "Vrancea",
            "București"
        ]
        indice_judet = random.randint(0, len(judete_romania) - 1)
        eliberare_buletin = "SPCLEP" + " " +judete_romania[indice_judet]
        return eliberare_buletin

    def generare_nume_prenume_tata(self):
        nume_prenume_tata = ""
        nrNumeTata = random.randint(1, 38265)
        nume = []
        file = open("NumeFamilieF.txt", "r", encoding="utf-8")
        if file == None:
            raise Exception("Fisierul nu a putut fi deschis")
        else:
            for linie in file:
                nume.append(linie.strip())
        numeTata = nume[nrNumeTata]
        nr_prenume = random.randint(1, 5)
        pren = []
        file = open("PrenumeBaieti.txt", "r", encoding="utf-8")
        if file == None:
            raise Exception("fisierul de prenume nu a putut fi deschis")
        else:
            for linie in file:
                pren.append(linie.strip())
        prenumeTata = ""
        for i in range(nr_prenume):
            index_prenume = random.randint(0, len(pren) - 1)
            prenumeTata += pren[index_prenume]
            prenumeTata += " "
        nume_prenume_tata = numeTata + " " + prenumeTata
        return nume_prenume_tata

    def generare_nume_mama(self):
        nume_prenume_mama = ""
        nrNumeMama = random.randint(1, 38265)
        nume = []
        file = open("NumeFamilieF.txt", "r", encoding="utf-8")
        if file == None:
            raise Exception("Fisierul nu a putut fi deschis")
        else:
            for linie in file:
                nume.append(linie.strip())
        numeMama = nume[nrNumeMama]
        nr_prenume = random.randint(1, 5)
        pren = []
        file = open("PrenumeFete.txt", "r", encoding="utf-8")
        if file == None:
            raise Exception("fisierul de prenume nu a putut fi deschis")
        else:
            for linie in file:
                pren.append(linie.strip())
        prenumeMama = ""
        for i in range(nr_prenume):
            index_prenume = random.randint(0, len(pren) - 1)
            prenumeMama += pren[index_prenume]
            prenumeMama += " "
        nume_prenume_mama = numeMama + " " + prenumeMama
        return nume_prenume_mama

# p1 = Persoana('M', 22)
# p2= Persoana('F', 19)
# print(p1)
# print(p2)

