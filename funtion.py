def full_name(firstName, lastName):
    return firstName + " " + lastName
firstname=input("Please input your first name : ")
lastname= input("Please input your last name : ")
fullname=full_name(firstname,lastname)
print(f"Your full name is : {fullname}")



#def number(first_number,second_numeber):
 #   return first_number + second_numeber
#fNumber=int(input("Please input first numbers : "))
#sNumber=int(input("Please input second numbers : "))
#result=number(fNumber,sNumber)
#print(f"Your result is : {result}")


#print("total students !!!")

#male=int(input("Please input total male : "))
#female=int(input("Please input total female"))
#total_member=number(male,female)
#print(f"Your total member of the class are : {total_member}")

from function_storage import *

print("Calculated !!!")
number1=int(input("Please input num1 : "))
number2=int(input("Please input num2 : "))
result=multiply(number1,number2)
print(result)