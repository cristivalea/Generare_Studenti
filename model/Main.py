import random
from datetime import date, timedelta

from model.Student import Student


def inscriere_facultate(data_start, data_end):
    '''
    :param data_start:
    :param data_end:
    :return: returneaza o lista de studenti
    pentru fiecare din zilele scurse dintre cele doua date se genereaza aleator numarul de studenti inscrisi in fiecare zi (100, 150)
    pentru o zi jumatate sunt fete si jumatate baieti
    baietii si fetele se adauga in lista
    '''
    lista_studenti = []
    diferenta_zile = (data_end - data_start).days
    print(diferenta_zile)
    if diferenta_zile == 0:
        raise Exception("Datele coincid")

    for i in range(diferenta_zile + 1):
        data_inmatriculare = data_start + timedelta(days=i)
        numar_studenti = random.randint(100, 150)
        numar_baieti = numar_studenti // 2
        numar_fete = numar_studenti - numar_baieti

        for _ in range(numar_baieti + numar_fete):
            while True:  # Asigură că data de naștere >= 1924
                varsta = random.randint(18, 25)
                anul_nasterii = data_inmatriculare.year - varsta
                if anul_nasterii >= 1924:
                    break

            gen = 'M' if _ < numar_baieti else 'F'
            student = Student(gen, varsta, data_inmatriculare)
            if student not in lista_studenti:
                lista_studenti.append(student)

    return lista_studenti

def lista_to_json(lista_studenti, data_start, data_end):
    cale_json = ""
    f = open("json_studenti.txt", "w", encoding="utf-8")
    for student in lista_studenti:
        j = student.prepare()
        lista_prenume = student.get_prenume()
        str_student = "D:\\PYTHON\\Generare_Studenti_Local\\Studenti_JSON\\"
        str_student += student.get_numeFamilie() + "_" + lista_prenume[0] + "_" + str(student.get_data_nastere().day) + "_"
        str_student += str(student.get_data_nastere().month) + "_" + str(student.get_data_nastere().year) + '.json\n'
        writer1 = f.write(str_student)
        f1 = open(str_student.strip(), "w", encoding="utf-8")
        writer = f1.writelines(student.prepare())
    return cale_json


start = date(2024, 2, 1)
end = date(2024, 2, 3)
# studenti = inscriere_facultate(start, end)
#
# for student in studenti:
#     print(student)
#
# print(f"Total studenti înscriși: {len(studenti)}")

lista_to_json(inscriere_facultate( start, end), start, end)

