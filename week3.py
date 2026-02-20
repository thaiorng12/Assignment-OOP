File=open("student_list.csv","a")
answer = "yes"
while answer == "yes" :
    username=input("Please input username : ")
    Password=input("Please input Password : ")
    fullName=input("Please input your fullName : ")
    gender=input("Please input your gender : ")
    years=input("Please input your study years :\n ")
File.write(username,Password,fullName,gender,years)
File.close()