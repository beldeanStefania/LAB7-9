from repository.Repository import Repository
from domain.student import Student

class repository_test:
    @staticmethod
    def test_repo():
        lista = Repository()
        lista.add(Student('4', 'ddd', '4'))
        lista.add(Student('3', 'ddd', '4'))
        lista.add(Student('1', 'ddd', '4'))
        lista.add(Student('2', 'ddd', '4'))
        lista.add(Student('6', 'ddd', '4'))
        assert lista.getById('4').getIdStudent() == '4'
        assert lista.getById('1').getIdStudent() == '1'
        assert lista.getById('1').getnume() == 'ddd'




test2 = repository_test()
test2.test_repo()
