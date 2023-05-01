from domain.student import Student

class testDomain():
    @staticmethod
    def testStudent():
        student = Student('1', 'aaaa', '5')
        assert student.getIdStudent()=='1'
        assert student.getgrup()=='5'



p = testDomain()
p.testStudent()