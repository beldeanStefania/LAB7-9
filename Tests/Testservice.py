from service.studentService import StudentService
from domain.student import Student
from repository.Repository import Repository
def testService():
    lista = Repository()
    service = StudentService(lista)
    service.addStudent('1', 'ddd', '5')
    service.addStudent('7', 'ddd', '5')
    gigel = service.getAllStudenti()
    for i in gigel:
        assert i.getnume() == 'ddd'



testService()