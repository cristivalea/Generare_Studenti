import random
import json
from datetime import date
from datetime import timedelta

from model.Competente import Competente
from model.Persoana import Persoana


class Student(Persoana):
    def __init__(self, sex, varsta, data_inmatriculare):
        super().__init__(sex, varsta)
        self.__data_inmatriculare = data_inmatriculare
        self.__nr_matricol = self.generare_numar_matricol()
        self.__cale_poze = self.citire_cai_fisier("cai_imagini.txt")
        self.__medie_bac = self.generare_medie_bac()
        self.__medie_mate = self.generare_medie_matematica()
        self.__medie_fizica = self.generare_medie_fizica()
        self.__medie_informatica = self.generare_medie_informatica()
        self.__competente = self.generare_calificative_competente()
        self.__medie_liceu = self.generare_medie_liceu()
        self.__nume_liceu = self.generare_nume_liceu()
        self.__recomandare_medic = self.generare_recomandare_medic()
        self.__data_adeverinta = self.generare_data_adeverinta()
        self.__data_achitare = self.__data_inmatriculare
        self.__scutire_taxa = self.generare_boolean()
        self.__alta_licenta = self.generare_boolean()
        self.__student_alta_facult = self.generare_boolean()
        self.__absolv_lic_inainte_an_curent = self.generare_boolean()
        self.__categ_speciale = self.generare_boolean()
        self.__Prog_studii_alta_limba = self.generare_boolean()
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

    def generare_medie_bac(self):
        medie_bac = random.randint(600, 1000) / 100
        return medie_bac

    def generare_medie_matematica(self):
        medie_mate = random.randint(600, 1000) / 100
        return medie_mate

    def generare_medie_fizica(self):
        medie_fizica = random.randint(600, 1000) / 100
        return medie_fizica

    def generare_medie_informatica(self):
        medie_informatica = random.randint(600, 1000) / 100
        return medie_informatica

    def generare_calificative_competente(self):
        comp = Competente()
        return comp

    def generare_medie_liceu(self):
        medie = random.randint(600, 1000) / 100
        return medie

    def generare_nume_liceu(self):
        licee = [
            "Colegiul Național Gheorghe Lazăr",
            "Colegiul Național Sfântul Sava",
            "Colegiul Național Mihai Viteazul",
            "Colegiul Național Spiru Haret",
            "Colegiul Național I. L. Caragiale",
            "Colegiul Național Bilingv George Coșbuc",
            "Colegiul Național Tudor Vianu",
            "Liceul Teoretic Jean Monnet",
            "Colegiul Național Mircea cel Bătrân",
            "Colegiul Național Alexandru Ioan Cuza",
            "Colegiul Național Vasile Alecsandri",
            "Colegiul Național Ferdinand I",
            "Colegiul Economic Virgil Madgearu",
            "Colegiul Național Emil Racoviță",
            "Liceul Teoretic Grigore Moisil",
            "Colegiul Național Emanuil Gojdu",
            "Liceul Teoretic Ovidius",
            "Colegiul Național Nicolae Bălcescu",
            "Colegiul Național Gheorghe Șincai",
            "Colegiul Tehnic Energetic",
            "Colegiul Național de Informatică Tudor Vianu",
            "Liceul Pedagogic Carmen Sylva",
            "Colegiul Național Andrei Șaguna",
            "Liceul de Arte Plastice Nicolae Tonitza",
            "Colegiul Național Moise Nicoară",
            "Colegiul Național Unirea",
            "Liceul Internațional de Informatică",
            "Colegiul Național Dragoș Vodă",
            "Liceul Sportiv Mircea Eliade",
            "Liceul Teoretic Nicolae Iorga"
        ]
        index = random.randint(0, len(licee) - 1)
        return licee[index]

    def generare_recomandare_medic(self):
        lista = ["apt", "inapt"]
        index = random.randint(0, 1)
        return lista[index]

    def generare_data_adeverinta(self):
        an = self.__data_inmatriculare.year
        luna = self.__data_inmatriculare.month
        zi = 0
        if luna in [1, 3, 5, 7, 8, 10, 12]:
            zi = random.randint(1, 31)
        elif luna in [4, 6, 9, 11]:
            zi = random.randint(1, 30)
        elif luna == 2 and an % 4 == 0:
            zi = random.randint(1, 29)
        elif luna == 2:
            zi = random.randint(1, 28)
        data = date(an, luna, zi)
        return data

    def generare_boolean(self):
        opt = ["true", "false"]
        index = random.randint(0, 1)
        return opt[index]

    def generare_scutire_taxa(self):
        opt = ["true", "false"]
        index = random.randint(0, 1)
        return opt[index]

    def get_medie_bac(self):
        return self.__medie_bac

    def get_medie_matematica(self):
        return self.__medie_mate

    def get_medie_fizica(self):
        return self.__medie_fizica

    def get_medie_informatica(self):
        return self.generare_nume_mama()

    def get_generare_competente(self):
        return self.__competente

    def get_medie_liceu(self):
        return self.__medie_liceu

    def get_nume_liceu(self):
        return self.__nume_liceu

    def get_recomandare_medic(self):
        return self.__recomandare_medic

    def get_data_adeverinta(self):
        return self.__data_adeverinta

    def data_achitare(self):
        return self.__data_achitare

    def get_scutire_taxa(self):
        return self.__scutire_taxa

    def get_alta_licenta(self):
        return self.__alta_licenta

    def get_student_alta_facult(self):
        return self.__student_alta_facult

    def get_abs_lic_ant_an_curent(self):
        return self.__absolv_lic_inainte_an_curent

    def get_categ_speciale(self):
        return self.__categ_speciale

    def get__prog_studii_alta_limba(self):
        return self.__Prog_studii_alta_limba

    #se tine cont de pozele cu B si F
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
            "Numar Matricol": self.__nr_matricol,
            "Nume": self.get_numeFamilie(),
            "Prenume": self.get_prenume(),
            "CNP": self.get_cnp(),
            "Serie Buletin": self.get_serie_buletin(),
            "Numar Prenume": self.get_nr_buletin(),
            "Adresa": {
                "Oras": self.generare_adresa().getOras(),
                "Strada": self.get_adresa().getStrada(),
                "Numar": self.get_adresa().getNumar(),
                "Bloc": self.get_adresa().getBloc(),
                "Apartament": self.get_adresa().getApartament()
            },
            "BuletinEliberat": self.get_eliberare_buletin(),
            "NumeTata": self.get_nume_tata(),
            "NumeMama": self.get_nume_mama(),
            "Data Nastere":{
                "Zi": self.get_data_nastere().day,
                "Luna": self.get_data_nastere().month,
                "An": self.get_data_nastere().year
            },
            "Data Inmatriculare": {
                "Zi": self.__data_inmatriculare.day,
                "Luna": self.__data_inmatriculare.month,
                "An": self.__data_inmatriculare.year
            },
            "MediaBAC": self.__medie_bac,
            "MedieMatematica": self.__medie_mate,
            "MedieFizica": self.__medie_fizica,
            "MedieInformatica": self.__medie_informatica,
            "Competente":{
                "OralRomana": self.get_generare_competente().get_romana(),
                "Digitale": self.get_generare_competente().get_digitale(),
                "LimbaMaterna": self.get_generare_competente().get_lb_materna(),
                "LingvisticeEngleza_Franceza":{
                    "IntelegereTextAudiat": self.get_generare_competente().get_com_lingvistice().get_audiat(),
                    "IntelegereTextCitit": self.get_generare_competente().get_com_lingvistice().get_citit(),
                    "MesajeScrise": self.get_generare_competente().get_com_lingvistice().get_scris(),
                    "MesajeOrale": self.get_generare_competente().get_com_lingvistice().get_orala(),
                    "InteractiuneOrala": self.get_generare_competente().get_com_lingvistice().get_interactiune_orala()
                }
            },
            "Medie_generala_liceu": self.__medie_liceu,
            "NumeLiceu": self.__nume_liceu,
            "RecomandareMedic": self.__recomandare_medic,
            "Data_eliberare_adeverinta_medicala": {
                "Zi": self.__data_adeverinta.day,
                "Luna": self.__data_adeverinta.month,
                "An": self.__data_adeverinta.year
            },
            "Suma_insccriere_achitata": "100",
            "Data_achitare": {
                "Zi": self.__data_inmatriculare.day,
                "Luna": self.__data_inmatriculare.month,
                "An": self.__data_inmatriculare.year
            },
            "Scutit de taxa": self.__scutire_taxa,
            "Alta_licenta": self.__alta_licenta,
            "Student_Alta_Facultate":self.__student_alta_facult,
            "Absolvire_liceu_inainte_an_curent": self.__absolv_lic_inainte_an_curent,
            "Categorii_speciale": self.__categ_speciale,
            "Program_studii_alta_limba": self.__Prog_studii_alta_limba,
            "Cale_poza": self.__cale_poze
        }
        j = json.dumps(x, ensure_ascii= False)
        return j

# student = Student('M', 23, date(2024, 2, 1))
# student2 = Student('F', 21, date(2024, 2, 3))
# student.prepare()
# student2.prepare()