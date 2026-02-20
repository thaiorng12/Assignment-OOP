class People:
    def __init__(self,Type,ID,Name,Dob,Gender,Title):
        self.type=Type
        self.id=ID
        self.name=Name
        self.dob=Dob
        self.gender=Gender
        self.title=Title
    def CheckoutBook(self):
        print(self.type," : ",self.name, "has been checkedout a book ")
    def CheckinBook(self):
        print(self.type," : ",self.name, "has been checkin a book ")
class Librarian:
    def __init__(self,ID,Name,Gender):
        self.id=ID
        self.name=Name
        self.gender=Gender
class book: 
    def __init__(self,ID,Title):
        self.id=ID
        self.title=Title

name = input("Please input your name : ")
student=People("Student","12345",name,"18/7/2004","male",)
student.CheckoutBook()