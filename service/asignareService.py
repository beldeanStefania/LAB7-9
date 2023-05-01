from domain.asignare import Asignare
from repository.Repository import Repository
from repository.asignareRepository import AsignareRepository


class AsignareService:
    def __init__(self, asignareRepository: AsignareRepository, studentRepository: Repository):
        self.__repository = asignareRepository
        self.__student_repository = studentRepository

    def addAsignare(self, idAsignare, idStudent, idpb, idlab, nota):
        """
        adauga o lista cu id-ul, numarul problemei, numarul laboratorului si notele studentului
        :param idStudent: string
        :param idpb: string
        :param idlab: string
        :param nota: string
        :return:
        """
        entitate = Asignare(idAsignare, idStudent, idpb, idlab, nota)#fara idlab
        self.__repository.add(entitate)

    def getAllAsignari(self):
        return self.__repository.getAll()

    def find(self):
        """
        cauta daca exista id-ul studentului
        :return:
        """
        return self.__repository.getAll()

    def notare(self, idStudent, idpb, idlab, nota):
        """
        adauga note studentului cu id-ul dat
        :param idStudent: string
        :param idpb: string
        :param idlab: string
        :param nota: string
        :return:
        """
        lista = [*self.__repository.getAll()]
        for i in lista:
            if i.getIdAsignare() == idStudent and i.getIdpb() == idpb and i.getIdLab() == idlab:
                i.setNota(nota)

        # def SortareNume(self, variabila):
        """dictionar ={}
        lista = [*self.__repository.getAll()]
        for nume in lista:
            student_nume = self.__repository.getById(variabila).getnume()"""

    def numeStudent(self, idStudent):
        lista = self.__student_repository.getAll()
        for i in lista:
            if i.getId() == idStudent:
                return i.getnume()

    def Sortare(self, param):
        studenti = {}
        lista_studenti = self.__repository.getAll()
        for i in lista_studenti:
            student_nume = self.numeStudent(i.getId())
            nota = i.getNota()
            studenti[student_nume] = nota
        if param == '1':
            sortari = {key: val for key, val in sorted(studenti.items(), key=lambda d: d[0])}
        elif param == '2':
            sortari = sorted(studenti.items(), key=lambda d: d[1])
        return sortari

    def Medie(self,idStudent):
        m = 0
        nr = 0
        lista = [*self.__repository.getAll()]
        for studenti in lista:
            if studenti.getId() == idStudent:
                m = m + studenti.getNota()
                nr = nr + 1
        m = m // nr
        return m
    def Lista_studenti(self):
        lista = [*self.__repository.getAll()]
        lista_studenti = []
        for student in lista:
            if student.getId() in lista_studenti:
                print("Se afla deja")
            else:
                lista_studenti.append(student.getId())

    def Medie_sub5(self):
        entitate = self.Lista_studenti()
        for student in entitate:
            if self.Medie(student) <= 5:
                return self.numeStudent(student)

