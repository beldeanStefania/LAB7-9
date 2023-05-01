class Asignare:
    def __init__(self, idAsignare, idStudent, idpb, idlab, nota):
        self.__idAsignare = idAsignare
        self.__idStudent = idStudent
        self.__idpb = idpb
        self.__idlab = idlab
        self.__nota = nota

    def getIdAsignare(self):
        return self.__idAsignare

    def getIdpb(self):
        return self.__idpb

    def getIdLab(self):
        return self.__idlab

    def getNota(self):
        return self.__nota

    def setIdAsignare(self, idStudent):
        self.__idStudent = idStudent

    def setIdpd(self, idpb):
        self.__idpb = idpb

    def setIdLab(self, idlab):
        self.__idlab = idlab

    def setNota(self, nota):
        self.__nota = nota

    def __str__(self):
        return f"id: {self.__idStudent}, id problema: {self.__idpb}, id laborator: {self.__idlab}, nota:{self.__nota}"



