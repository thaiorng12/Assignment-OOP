File=open("student_list.csv","a")
def studentData():
    FirstName=input("Please input your FirstName: ")
    LastName=input("Please input your LastName: ")
    Email=input("Please input your Email: ")
    Password=input("Please input your Password: ")
    File.write(f"{FirstName},{LastName},{Email},{Password}\n")
    isExit=input("do you want to continues ? ")
    return isExit
if studentData()=="yes":
    studentData()
File.close()
