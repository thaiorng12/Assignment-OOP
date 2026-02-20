class people:
    def __init__(self,Type,ID,Name,Dob,Gender,BookTitle):
        self.type=Type
        self.id=ID
        self.name=Name
        self.dob=Dob
        self.gender=Gender
        self.title=BookTitle
    def CheckoutBook(self):
        print(self.type," : ",self.name, "has been checkedout a book ")
    def CheckinBook(self):
        print(self.type," : ",self.name, "has been checkin a book ")
    def BookRecord(self):
        pass
    def Record(self):
        pass
class Librarian(people):
    def BookRecord(self):
        print(f"{self.name} ID : {self.id} has been borrowed the book from the library . ")
class Book(people):
    def Record(self):
        print(f"Book's Title: {self.title} ID : {self.id} has been borrowed by {self.name}")
name = input("Please input your name : ")
student=people("student","B20251345",name,"18/08/2000","Male","The Secret")
librarian=Librarian("student","B20251345",name,"18/08/2000","Male","The Secret")
book=Book("student","B20251345",name,"18/08/2000","Male","The Secret")

print("--- Record ---\n")
student.CheckoutBook()
librarian.BookRecord()
book.Record()
print("\n")