from repository.asignareRepository import AsignareRepository
from repository.Repository import Repository
from service.asignareService import AsignareService
from service.problemaService import ProblemaService
from service.studentService import StudentService
from ui.consola import Consola

#from Tests.Test_nou_domain import TestNouDomainStudent
#from Tests.Test_nou_domain import TestNouDomainProblema
#from Tests.Test_nou_domain import TestNouDomainAsignare
#from Tests.Test_nou_repository import TestNouAsignareRepository
#from Tests.Test_nou_repository import TestNouRepository


def main():
    studentRepository = Repository()
    problemaRepository = Repository()
    repository = AsignareRepository()
    asignareService = AsignareService(repository, studentRepository)
    studentService = StudentService(studentRepository)
    problemaService = ProblemaService(problemaRepository)
    consola = Consola(studentService, problemaService, asignareService)


    consola.Menu()

main()