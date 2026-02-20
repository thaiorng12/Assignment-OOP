def calculate_total(*args, tax_rate=0):
    subtotal = sum(args)
    total = subtotal + (subtotal * tax_rate / 100)
    return total

name = input("Enter your name: ")
total_amount = calculate_total(10, 20, 30, tax_rate=5)
print(f"Hello {name}, your total is ${total_amount}")

