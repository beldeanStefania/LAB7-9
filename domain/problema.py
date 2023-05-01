from domain.asignare import Asignare


class ProbLab():
    def __init__(self, numarlab, numarprob, descriere, deadline):
        self.__numarlab = numarlab
        self.__numarprob = numarprob
        self.__descriere = descriere
        self.__deadline = deadline

    def getId(self):
        return self.__numarlab

    def setId(self, id):
        self.__id = id

    def getNrProb(self):
        return self.__numarprob

    def getDescriere(self):
        return self.__descriere

    def getDeadline(self):
        return self.__deadline

    def setNumarProb(self, numarprob_new):
        self.__numarprob = numarprob_new

    def setDescriere(self, descriere_new):
        self.__descriere = descriere_new

    def setDeadline(self, deadline_new):
        self.__deadline = deadline_new

    def __str__(self):
        return f"numar lab: {self.__numarlab}, numar prob: {self.__numarprob}, descriere: {self.__descriere}, deadline: {self.__deadline}"