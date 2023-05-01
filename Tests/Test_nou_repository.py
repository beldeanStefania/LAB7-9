from domain.student import Student
from repository.Repository import Repository
from repository.asignareRepository import AsignareRepository


class TestNouAsignareRepository():
    @staticmethod
    def testAsignareRepository():
        dictionar = {}
        lista = AsignareRepository()
        lista.add(Student('4', 'ddd', '4'))
        lista.add(Student('3', 'ddd', '4'))
        lista.add(Student('1', 'ddd', '4'))
        lista.add(Student('2', 'ddd', '4'))
        lista.add(Student('6', 'ddd', '4'))
        assert lista.getById('4').getId() == '4'
        assert lista.getById('1').getId() == '1'
        assert lista.getById('1').getnume() == 'ddd'

class TestNouRepository():
    @staticmethod
    def testRepository():
        entitate =  {}
        lista = Repository()
        lista.add(Student('1', 'dfs', '5'))
        lista.add(Student('3', 'ddd', '4'))
        lista.add(Student('7', 'ddd', '4'))
        lista.add(Student('2', 'ddd', '4'))
        lista.add(Student('6', 'ddd', '4'))
        assert lista.getById('1').getId() == '1'
        assert lista.getById('6').getId() == '6'
        assert lista.getById('3').getnume() == 'ddd'


a = TestNouAsignareRepository()
a.testAsignareRepository()
b = TestNouRepository()
b.testRepository()
