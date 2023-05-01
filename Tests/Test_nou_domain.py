from domain.asignare import Asignare
from domain.problema import ProbLab
from domain.student import Student


class TestNouDomainStudent():
    @staticmethod
    def testStuddnt():
        student = Student('1', 'Stefi', '3')
        assert student.getId() == '1'
        assert student.getnume() == "Stefi"
        assert student.getgrup() == '3'

class TestNouDomainProblema():
    @staticmethod
    def testProblema():
        prob = ProbLab('1', '3', 'descriere problema', '30.12')
        assert prob.getId() == '1'
        assert prob.getNrProb() == '3'
        assert prob.getDescriere() == 'descriere problema'
        assert prob.getDeadline() == '30.12'

class TestNouDomainAsignare():
    @staticmethod
    def testAsignare():
        asignare = Asignare('1', '2', '1', '10')
        assert asignare.getIdAsignare() == '1'
        assert asignare.getIdpb() == '2'
        assert asignare.getIdLab() == '1'
        assert asignare.getNota() == '10'

x = TestNouDomainStudent()
x.testStuddnt()
y = TestNouDomainProblema()
y.testProblema()
z = TestNouDomainAsignare()
z.testAsignare()
