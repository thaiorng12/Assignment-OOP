class teacher :
    def __init__(self,Name,ID,Gender,Major,Working_exp,DOB):
        self.name=Name
        self.id=ID
        self.gender=Gender
        self.major=Major
        self.working_exp=Working_exp
        self.dob=DOB
    def working(self):
        print(f"professor \"{self.name}\" is attending to the class now")
class student :
    def __init__(self,Name,ID,Gender,Major,DOB):
        self.name=Name
        self.id=ID
        self.gender=Gender
        self.major=Major
        self.dob=DOB
class staff :
    def __init__(self,Name,ID,Gender,DOB,Shift,YearsWorking,
                 department):
        self.name=Name
        self.id=ID
        self.gender=Gender
        self.dob=DOB
        self.shift=Shift
        self.yearsworking=YearsWorking
class cleaner :
    def __init__(self,Name,ID,Gender,Shift,DOB):
        self.name=Name
        self.id=ID
        self.gender=Gender
        self.shift=Shift
        self.dob=DOB
name = input("input your name : ")
Teacher = teacher(name,"12345","Male","IT","10 years","18/03/1990")
Teacher.working()
        