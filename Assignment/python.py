import os

file = "storage.csv"

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear ')

def team():
    print("====Team Members====")
    print("1. Chorn Vibol ID: B20250366 ")
    print("2. Chhour Thaiorng ID: B20251345")
    print("3. Ther Raksa ID: B20251115")
    print("4. Sok Kanha  ID: B20240431")
    print("5. Pha Somony ID: B20250145")

def log_in():
    counter = 0
    while True:
        print("====Login====")
        try :
            username = input("Please Enter username: ")
        except ValueError:
            print("Invalid input. Please enter a valid username.")
        try :
            password = input("Please Enter password: ")
        except ValueError:
            print("Invalid input. Please enter a valid password.")
        if username == "admin" and password == "12345":
            print("Login successful!")
            break
        else:
            counter += 1
            print("Invalid username or password. Please try again.")
            print(f"you have {3 - counter} attempts left.")
        if counter >= 3:
            print("Too many failed attempts. Please try again later.")
            break

def Create():
    with open(file, "w") as f:
        f.write(" Student ID  ,  Name  ,  Date of Birth  ,  Gender  ,  Department\n")
    print("File created successfully!")

def Read():
    if not os.path.exists(file):
        print("File does not exist. Please create the file first.")
        return
    with open(file, "r") as f:
        content = f.read()
        print(content)

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    gender = input("Enter gender: ")
    department = input("Enter department: ")
    with open(file, "a") as f:
        f.write(f"{student_id },{name },{dob },{gender },{department }\n")
    print("Student added successfully!")

def search_student():
    if not os.path.exists(file):
        print("File does not exist. Please create the file first.")
        return
    student_id = input("Enter student ID to search: ")
    with open(file, "r") as f:
        for line in f:
            if line.startswith(student_id):
                print("Student found:", line.strip())
                return
    print("Student ID not found.")
def Update():
    if not os.path.exists(file):
        print("File does not exist. Please create the file first.")
        return
    student_id = input("Enter student ID to update: ")
    lines = []
    found = False
    with open(file, "r") as f:
        for line in f:
            if line.startswith(student_id):
                found = True
                print("Current record:", line.strip())
                choice = input("Which field do you want to update? (name/dob/gender/department): ").strip().lower()
                if choice == "name":
                    new_value = input("Enter new name: ")
                    line = f"{student_id},{new_value},{line.split(' , ')[2]},{line.split(' , ')[3]},{line.split(' , ')[4]}"
                elif choice == "dob":
                    new_value = input("Enter new date of birth (YYYY-MM-DD): ")
                    line = f"{student_id},{line.split(' , ')[1]},{new_value},{line.split(' , ')[3]},{line.split(' , ')[4]}"
                elif choice == "gender":
                    new_value = input("Enter new gender: ")
                    line = f"{student_id},{line.split(' , ')[1]},{line.split(' , ')[2]},{new_value},{line.split(' , ')[4]}"
                elif choice == "department":
                    new_value = input("Enter new department: ")
                    line = f"{student_id},{line.split(' , ')[1]},{line.split(' , ')[2]},{line.split(' , ')[3]},{new_value}"
                else:
                    print("Invalid choice. No changes made.")
            lines.append(line)
    if found:
        with open(file, "w") as f:
            f.writelines(lines)
        print("Student record updated successfully!")

   

def Delete():
    pass