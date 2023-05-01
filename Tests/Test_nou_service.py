from service.asignareService import AsignareService


class TestNouAsignareService():
    @staticmethod
    def testAsignareService():
        dictionar = {}
        lista = AsignareService()
        lista.addAsignare('1', '2', '1', '10')
        assert len(lista) == 1
        #lista.addAsignare('1', '2', '1', '10')

c = TestNouAsignareService()
c.testAsignareService()
