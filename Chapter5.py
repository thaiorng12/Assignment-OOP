def func(arg, vat):
    return arg *(100 + vat)/100
numbers = (10,20,30)
total = sum(numbers)
result = func(total,vat=5)
Name= input("Please input your name : ")
print(f"Hello {Name}, your total is ${result} ")


