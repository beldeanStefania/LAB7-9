from domain.exceptii.duplicateError import DuplicateError
from domain.student import Student

class AsignareRepository:
    def __init__(self):
        self.__dictionar = {}

    def getAll(self):
        '''
        returneza o lista de studenti
        :return: o lista de obiecte de tipul student
        '''
        return list(self.__dictionar.values())

    def getById(self, idEntitate):
        '''
        cauta un student dupa id
        :param idEntitate: string
        :return: un student daca exista id-ul sau None in caz contrar
        '''
        if idEntitate in self.__dictionar:
            return self.__dictionar[idEntitate]
        return None

    def add(self, entitate):
        """
        adauga lista in dictionar
        :param entitate: o lista
        :return:
        """
        if self.getById(entitate.getIdAsignare()):
            raise DuplicateError("Exista deja un student cu id-ul dat")
        self.__dictionar[entitate.getIdAsignare()] = entitate

    def modify(self, entitate):
        '''
        modifica un student dupa id
        :param entitate:
        :return:
        '''
        if self.getById(entitate.getIdAsignare()) is None:
            raise KeyError("Nu exista niciun student cu id-ul dat")
        self.__dictionar[entitate.getIdAsignare()] = entitate

    def modifyName(self, entitate):
        '''
        modifica un student dupa nume
        :param studentNou:
        :return:
        '''
        self.__dictionar[entitate.getIdAsignare()] = entitate

    def delete(self, entitate):
        '''
        sterge un student dupa id
        :param entitate: string
        :return:
        '''
        if self.getById(entitate) is None:
            raise KeyError("Nu exista niciun student cu id-ul dat")
        self.__dictionar.pop(entitate)