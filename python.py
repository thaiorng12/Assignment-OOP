def clearscreen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear ')

answer = "yes"
Product_items_names = [ "Television","Air Conditioner","refrigerator"]
while answer =="yes" or answer =="Yes" :
    print ("---- Shopping Cart System ----\n")
    print("1. View cart ")
    print("2. Add item ")
    print("3.Remove item")
    print("4. Update item")
    print("5. view number of items ")
    print("6. Exit\n")

    try:
        Choice = int(input("Please input your choice : "))
    except ValueError : 
        clearscreen()
        print("Invalid input , Please select only number between 1 —— 6\n")
        continue

    if Choice == 1:
        clearscreen()
        print("1. View cart ")
        print(f"my cart :{Product_items_names}\n")

    elif Choice == 2:
        clearscreen()
        print("2. Add item ")
        print(Product_items_names)
        Add_item = str(input("Please Add item to your cart : "))
        Product_items_names.append(Add_item)
        print(f"my cart :{Product_items_names}\n")

    elif Choice == 3:
        clearscreen()
        print("3.Remove item")
        print(Product_items_names)
        Remove_item = str(input("Please input the item that you want to remove : "))
        if Remove_item in Product_items_names :
            Product_items_names.remove(Remove_item)
            print(f"You have remove {Remove_item} from your Cart")
            print(f"Your cart : {Product_items_names}\n")
        else : 
            print("Invalid items\nthis item is not in your cart \n")

    elif Choice == 4:
        clearscreen()
        try :
            print("4. Update item")
            print(Product_items_names)
            index = int(input("Please input number of index that you want to update : "))
            if 0 < index < len(Product_items_names):
                print(Product_items_names[index])
                Update_item = str(input("Please input which item you want to update : "))
                Product_items_names[index] = Update_item
                print("Your list cart have been updated")
                print(f"Your cart now : {Product_items_names}\n")
            else : print("Invalid Index Please again Later\n")
        except ValueError:
            print("Invalid , Please input only Number \n")

    elif Choice == 5:
        clearscreen()
        print("5. view number of items ")
    
        print(f"Your items in your cart now has {len(Product_items_names)} items \n")

    elif Choice == 6:
        clearscreen()
        print("Exiting ...")
        break

    else :
        clearscreen()
        print("Invalid Choice , Please choose between number 1 —— 6")

    answer = input("Do you want to continues ? Yes or No ")
    clearscreen()