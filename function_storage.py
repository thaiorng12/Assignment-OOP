def multiply(num1,num2):
    return num1 + num2 

def matrix_mul(a,b):
    return[
        [sum(i * j for i , j in zip(r,c))for c in zip(*b)] for r in a
    ]
a =[[1,2],[3,4]]
b =[[5,1],[2,1]]
c = matrix_mul(a,b)

#print (c)

def calculate_price_with_vat(price, vat):
    
    return price *(100 + vat ) /100

price = int(input("Please input the product price : "))
vat = 10
total = calculate_price_with_vat(price,vat)
print(f"")
print (f"your total price is {total}$")


