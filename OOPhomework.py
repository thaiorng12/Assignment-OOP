class People:
    def __init__(self,Type,ID,Name,Dob,Gender):
        self.type=Type
        self.id=ID
        self.name=Name
        self.dob=Dob
        self.gender=Gender
    def CheckoutBook(self):
        print(self.type," : ",self.name, "has been checkedout a book ")
    def CheckinBook(self):
        print(self.type," : ",self.name, "has been checkin a book ")
class Librarian:
    def __init__(self,ID,Name,Gender):
        self.id=ID
        self.name=Name
        self.gender=Gender
    def BookRecord(self):
        print(f"{self.name} ID:{self.id} has been borrowed the book from the library . ")
class book: 
    def __init__(self,ID,Title,Name):
        self.id=ID
        self.title=Title
        self.name=Name
    def Record(self):
        print(f"Book's Title: {self.title} ID : {self.id} has been borrowed by {self.name}")

name = input("Please input your name : ")
student_ID = input("Please input your ID : ")
student=People("Student",student_ID,name,"18/7/2004","male",)
librarian = Librarian(student_ID,name,"male")
Book = book("865431","The Secret",name)
print("--- Record ---\n")
student.CheckoutBook()
librarian.BookRecord()
Book.Record()

        