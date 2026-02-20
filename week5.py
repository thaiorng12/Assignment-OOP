#def sum_number(*num):
  #  print(sum(num))
#num1 = int(input("Please input num1"))
#num2 = int(input("Please input num2"))
#sum = num1 + num2 
#sum_number(20,30,50)
#def sum_number(num1,num2):
#    return num1 + num2
#Num1 = int(input("Plese input num1 : "))
#Num2 = int(input("Plese input num2 : "))
#total =sum_number(Num1,Num2)
#print(total)

#def describe_pet(animal, name):
#    print(f"I have a {animal} named {name}")
#describe_pet(name="kiki",animal="dog")

#def user_profile(**data):
 #   print("user city is : " + data["city"])
#user_profile(name="sovan",city='Phnom Penh', age=25)

#def my_country(country="cambodia") :
 #   print("I am from "+ country)
#my_country("Japan")
#my_country("China")
#my_country()

#name= input("Enter name : ")
#print(f"Length of name : {sum(name)}")

#factorial 
#def factorial(n):
#    if n ==1 :
#        return 1
#    else :
#        return n * factorial(n-1)
#print(factorial(5))


# A lamda that adds 10 to input 'a'
#x = lambda a : a + 10
#print(x(5))


#A function that returns a lamda function
#def myfunc(n):
#    return lambda a : a * n
#mydoubler=myfunc(2)

#print(mydoubler(11))


x = 25

def outer():
    global x
    y = 24
    x +=1

    def inner():
        z ="local"
        print(x,y,z)
    inner()