from domain.exceptii.duplicateError import DuplicateError


class Repository:
    def __init__(self):
        self.__entitati = {}

    def getAll(self):
        '''
        returneza o lista de studenti
        :return: o lista de obiecte de tipul student
        '''
        return list(self.__entitati.values())

    def getById(self, idEntitate):
        '''
        cauta un student dupa id
        :param idEntitate: string
        :return: un student daca exista id-ul sau None in caz contrar
        '''
        if idEntitate in self.__entitati:
            return self.__entitati[idEntitate]
        return None

    def add(self, entitate):
        """
        adauga un student(entitatea) in dictionar si verifica daca studentul exista deja sau nu in lista
        :param entitate: lista du id-ul, numele si grupa din care face parte studentul
        :return: None daca studentul exista deja in lista
        """
        if self.getById(entitate.getId()) is not None:
            raise DuplicateError("Exista deja un student cu id-ul dat")
        self.__entitati[entitate.getId()] = entitate

    def modify(self, entitate):
        '''
        modifica un student dupa id
        :param entitate: lista du id-ul, numele si grupa din care face parte studentul
        :return: None daca studentul nu se afla in lista
        '''
        if self.getById(entitate.getId()) is None:
            raise KeyError("Nu exista niciun student cu id-ul dat")
        self.__entitati[entitate.getId()] = entitate

    def modifyName(self, entitate):
        '''
        modifica un student dupa nume
        :param studentNou:
        :return:
        '''
        self.__entitati[entitate.getId()] = entitate

    def delete(self, entitate):
        '''
        sterge un student dupa id
        :param entitate: string
        :return: None daca nu exista niciun student cu id-ul dat
        '''
        if self.getById(entitate) is None:
            raise KeyError("Nu exista niciun student cu id-ul dat")
        self.__entitati.pop(entitate)
