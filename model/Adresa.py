class Adresa:
    def __init__(self, oras, strada, numar, bloc, apartament):
        self.__oras = oras
        self.__strada = strada
        self.__numar = numar
        self.__bloc = bloc
        self.__apartament = apartament

    def getOras(self):
        return self.__oras

    def getStrada(self):
        return self.__strada

    def getNumar(self):
        return self.__numar

    def getBloc(self):
        return self.__bloc

    def getApartament(self):
        return self.__apartament

    def __repr__(self):
        string = self.__oras + " " + self.__strada + " " + str(self.__numar) + " " + str(self.__bloc) + " " + str(self.__apartament)
        return string