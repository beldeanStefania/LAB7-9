from domain.asignare import Asignare


class Student():
    def __init__(self, idStudent, nume, grup):
        self.__idStudent = idStudent
        self.__nume = nume
        self.__grup = grup

    def getId(self):
        return self.__idStudent

    def setId(self, id):
        self.__idStudent = id

    def getnume(self):
        return self.__nume

    def getgrup(self):
        return self.__grup

    def setnume(self, nume):
        self.__nume = nume

    def setgrup(self, grup):
        self.__grup = grup

    def __str__(self):
        return f"id: {self.__idStudent}, nume: {self.__nume}, grupa: {self.__grup}"

