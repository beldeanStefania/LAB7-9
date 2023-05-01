from domain.exceptii.duplicateError import DuplicateError
from service.asignareService import AsignareService
from service.problemaService import ProblemaService
from service.studentService import StudentService
from repository.Repository import Repository


class Consola:
    def __init__(self, studentService: StudentService, problemaService: ProblemaService, asignareServive : AsignareService):
        self.__studentService = studentService
        self.__problemaService = problemaService
        self.__asignareService = asignareServive
        self.__repository = Repository()

    def AddStudent(self):
        """
        adauga un student in lista
        :return:
        """
        try:
            id = input("Dati id-ul studentului: ")
            nume = input("Dati numele studentului: ")
            grupa = input("Dati grupa din care face parte studentul: ")
            self.__studentService.addStudent(id, nume, grupa)
        except DuplicateError as e:
            print(e)

    def AddPb(self):
        """
        adauga problema in lista
        :return:
        """
        try:
            nrlab = input("Scrieti numarul laboratorului: ")
            nrpb = input("Scrieti numarul problemei: ")
            descriere = input("Descriere: ")
            deadline = input("Data scadenta: ")
            self.__problemaService.addPb(nrlab, nrpb, descriere, deadline)
        except DuplicateError as e:
            print(e)

    def ModifyStudent(self):
        """
        modifica datele studentului
        :return:
        """
        try:
            id = input("Dati id-ul studentului existent: ")
            numeNou = input("Dati noul nume al studentului: ")
            grupa = input("Dati noua grupa din care face parte studentul: ")
            self.__studentService.modifyStudent(id, numeNou, grupa)
        except KeyError as e:
            print(e)

    def ModifyPb(self):
        """
        modifica laboratorul si problema/problemele pe care le are studentul
        :return:
        """
        #ok=bool(input("Doriti sa modificati si numarul laboratorului? "))
        #if ok == "da":
        nrlab = input("Dati numarul laboratorului existent: ")
        nrpb = input("Dati noul numar al problemei: ")
        descriere = input("Dati noua descriere: ")
        deadline = input("Dati noul termen: ")
        self.__problemaService.modifypb(nrlab, nrpb, descriere, deadline)

    def DeleteStudent(self):
        """
        sterge studentul din lista
        :return:
        """
        try:
            id = input("Dati id-ul studentului de sters: ")
            self.__studentService.deleteStudent(id)
        except KeyError as e:
            print(e)

    def DeletePb(self):
        """
        sterge problemele pe care le are studentul
        :return:
        """
        nrlab = input("Dati numarul laboratorului")
        self.__problemaService.delete(nrlab)

    def printAll(self, entitati):
        """
        afiseaza toata lista cu studenti
        :param entitati:
        :return:
        """
        for entitate in entitati:
            print(entitate)

    def printAsignari(self, entitati):
        """
        afiseaza notele studentului
        :param entitati:
        :return:
        """
        for entitate in entitati:
            print(entitate)

    def printAllP(self, entitati):
        """
        afiseaza lista cu laboratoare si probleme
        :param entitati:
        :return:
        """
        for entitate in entitati:
            print(entitate)

    def AddAsignare(self):
        """
        atribuie unui strudent cate o problema
        :return:
        """
        try:
            idAsignare = input("Scrieti id-ul asignarii: ")
            nrlab = input("Scrieti numarul laboratorului: ")#doar idAsignare, idlab, idpb
            nrpb = input("Scrieti numarul problemei: ")
            idStudent = input("Id Student: ")
            nota = input("Scrieti nota: ")
            self.__asignareService.addAsignare(idAsignare, idStudent, nrpb, nrlab, nota)
        except DuplicateError as e:
            print(e)

    def Notare(self):
        """
        atribuie unui student o notq
        :return:
        """
        try:
            nrlab = input("Scrieti numarul laboratorului")
            nrpb = input("Scrieti numarul problemei")
            idStudent = input("Id Student:")
            if self.__repository.getById(idStudent) is None:
                raise KeyError("Gresit, cred")
            nota = input("Nota noua")
            self.__asignareService.notare(nrlab, nrpb, idStudent, nota)
        except DuplicateError as e:
            print(e)

    def SortNume(self):
        param = input("Scrie '1' pentru sortare dupa nume si '2' pentru sortare dupa nota: ")
        print(self.__asignareService.Sortare(param))

    def Sortare(self):
        print(self.__asignareService.Medie_sub5())


    def printMenu(self):
        print("1. Adauga student")
        print("2. Adauga problema")
        print("3. Modifica lista de studenti")
        print("4.Modifica lita de probleme")
        print("5. Sterge student")
        print("6. Sterge problema")
        print("7.Asignare")
        print("8. Notare")
        print("9. Sorteaza studentii: 1. Dupa nume")
        print("                       2. Dupa nota")
        print("10. Afiseaza toti studentii cu media notelor mai mica decat 5")
        print("a. Afisare")
        print("b. Afisare asignare")

    def Menu(self):
        while True:
            self.printMenu()
            option = input("Scrieti optiunea: ")
            if option == "1":
                self.AddStudent()
            if option == "2":
                self.AddPb()
            elif option == "3":
                self.ModifyStudent()
            elif option == "4":
                self.ModifyPb()
            elif option == "5":
                self.DeleteStudent()
            elif option == "6":
                self.DeletePb()
            elif option =="7":
                self.AddAsignare()
            elif option == "8":
                self.Notare()
            elif option == "9":
                self.SortNume()
            elif option == "10":
                print(* self.__asignareService.find(), sep='\n')
            elif option =="11":
                self.Sortare()
            elif option == "a":
                self.printAll(self.__studentService.getAllStudenti())
                self.printAllP(self.__problemaService.getAllProbleme())
            elif option == "b":
                self.printAsignari(self.__asignareService.getAllAsignari())
