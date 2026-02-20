print("------Article Management System-------")
print("1. Show All Article ")
print("2. Access Article By Index ")
print("3. Access Article By negative Index ")
print("4. Add New Article ")
print("5. Add New Article by specify column ")
print("6. update New Article ")
print("--------------------------------------")

def test():
    choice = int(input("enter your choice :"))
    List = ["apple","banana","pineapple"]
    if choice == 1:
        print(List)
    elif choice ==2:
        index = int(input("Please specify index you wish to access : "))
        print(List[index])
    elif choice ==3:
        Negative_Index = int(input("Please specify Negative index you wish to acess: "))
        print(List[Negative_Index])
    elif choice ==4:
         new_article = input("Please input New Article : ")
         List.append(new_article)
         print(List)
    elif choice ==5:
         new_article = input("Please input New Specify Article : ")
         where_to_insert = int(input("please input the number where to insert"))
         print(List)
         List.insert(where_to_insert,new_article)
         print(List)
    elif choice ==6:
        index = int(input("Please input an Index numeber : "))
        Update_Article = input("Please update new Article : ")
        print(List)
        List[index]=Update_Article
        print(List)
n = "yes"
while n !="no":
    test()
    n = input("do you want to do it again ? yes or no ")
print("bye")
