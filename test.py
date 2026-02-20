answer = "yes"
Product_items_names = ["Television", "Air Conditioner", "Refrigerator"]

while answer.lower() == "yes":
    print("---- Shopping Cart System ----\n")
    print("1. View cart")
    print("2. Add item")
    print("3. Remove item")
    print("4. Update item")
    print("5. View number of items")
    print("6. Exit\n")

    try:
        Choice = int(input("Please input your choice : "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    if Choice == 1:
        print("Your cart:", Product_items_names)

    elif Choice == 2:
        Add_item = input("Please add item to your cart : ")
        Product_items_names.append(Add_item)
        print("Your cart:", Product_items_names)

    elif Choice == 3:
        print("Your cart:", Product_items_names)
        Remove_item = input("Please input the item you want to remove : ")
        if Remove_item in Product_items_names:
            Product_items_names.remove(Remove_item)
            print(f"You have removed {Remove_item} from your cart.")
        else:
            print(f"{Remove_item} is not in your cart.")
        print("Your cart:", Product_items_names)

    elif Choice == 4:
        print("Your cart:", Product_items_names)
        try:
            index = int(input("Please input the index number to update : "))
            if 0 <= index < len(Product_items_names):
                print(f"Current item: {Product_items_names[index]}")
                Update_item = input("Please input the new item : ")
                Product_items_names[index] = Update_item
                print("Your cart has been updated:", Product_items_names)
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

    elif Choice == 5:
        print(f"Your cart has {len(Product_items_names)} items.")

    elif Choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please select between 1 and 6.")

    answer = input("Do you want to continue? Yes or No: ")