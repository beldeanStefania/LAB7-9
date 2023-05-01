from domain.problema import ProbLab
from repository.Repository import Repository


class ProblemaService:
    def __init__(self, problemaRepository : Repository):
        self.__problemaRepository = problemaRepository

    def getAllProbleme(self):
        """
        returneaza lista de laboratoare si probleme
        :return:
        """
        return self.__problemaRepository.getAll()

    def addPb(self, nrlab, nrpb, descriere, deadline):
        """
        adauga o lista noua de probleme
        :param nrlab: string
        :param nrpb: string
        :param descriere: string
        :param deadline: string
        :return:
        """
        problema = ProbLab(nrlab, nrpb, descriere, deadline)
        self.__problemaRepository.add(problema)

    def modifypb(self, nrlab, nrpb, descriere, deadline):
        """
        modifica laboratorul, problema, descrierea si deadline-ul
        :param nrlab: string
        :param nrpb: string
        :param descriere: string
        :param deadline: string
        :return:
        """
        problema = ProbLab(nrlab, nrpb, descriere, deadline)
        self.__problemaRepository.modify(problema)

    def  delete(self, nrlab):
        """
        sterge laboratorul si problemele pe care le avea studentul
        :param nrlab:
        :return:
        """
        self.__problemaRepository.delete(nrlab)