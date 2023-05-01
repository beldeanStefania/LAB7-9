from domain.student import Student
from repository.Repository import Repository


class StudentService:
    def __init__(self, studentRepository : Repository):
        self.__studentRepository = studentRepository

    def getAllStudenti(self):
        """
        :return: lista cu toti studentii
        """
        return self.__studentRepository.getAll()

    def addStudent(self, id, nume, grupa):
        """
        adauga un student in lista
        :param id: string
        :param nume: string
        :param grupa: string
        :return:
        """
        student = Student(id, nume, grupa)
        self.__studentRepository.add(student)

    def modifyStudent(self, id, nume_nou, grupa):
        """
        modifica numele si grupa din care face parte un student
        :param id: string
        :param nume_nou: string
        :param grupa: string
        :return:
        """
        student = Student(id, nume_nou, grupa)
        self.__studentRepository.modify(student)

    def deleteStudent(self, id):
        """
        sterge un student dupa id
        :param id: string
        :return:
        """
        self.__studentRepository.delete(id)







