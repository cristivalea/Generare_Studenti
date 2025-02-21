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
        data_inmatriculare = date(data_start.year, data_start.month, data_start.day + i)
        print(data_inmatriculare)
        numar_studenti = random.randint(100, 150)
        numar_baieti = numar_studenti // 2
        numar_fete = numar_studenti - numar_baieti
        for b in range(numar_baieti):
            student = Student('M', random.randint(18, 25), data_inmatriculare)
            lista_studenti.append(student)

        for f in range(numar_fete):
            student = Student('F', random.randint(18, 25), data_inmatriculare)
            lista_studenti.append(student)

    return lista_studenti

start = date(2024, 2, 1)
end = date(2024, 2, 15)
studenti = inscriere_facultate(start, end)

for student in studenti:
    print(student)

print(f"Total studenti înscriși: {len(studenti)}")