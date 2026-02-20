File=open("student_list.csv", "a") 
def studentData():
    FirstName = input("Please input your FirstName: ")
    LastName = input("Please input your LastName: ")
    Email = input("Please input your Email: ")
    Password = input("Please input your Password: ")
    File.write(f"{FirstName},{LastName},{Email},{Password}\n")
    isExit = input("Do you want to continue? (yes/no): ")
    return isExit

while True:
        if studentData() != "yes":
            break
File.close()
