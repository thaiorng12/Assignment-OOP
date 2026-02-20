import json
import os

DATA_FILE = "students.json"


def load_data():
    """
    Load student data from the JSON file.
    Returns:
        list: A list of student records (dictionaries).
    """
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(students):
    """
    Save student data to the JSON file.
    Args:
        students (list): List of student records to save.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    """
    Add a new student record.
    Args:
        students (list): List of student records.
    """
    print("\n--- Add Student ---")
    name = input("Enter student name: ").strip()
    age = get_valid_int("Enter student age: ")
    student_id = input("Enter student ID: ").strip()

    student = {"id": student_id, "name": name, "age": age}
    students.append(student)
    print("Student added successfully!")


def view_students(students):
    """
    Display all student records.
    Args:
        students (list): List of student records.
    """
    print("\n--- Student List ---")
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")


def search_student(students):
    """
    Search for a student by ID.
    Args:
        students (list): List of student records.
    """
    print("\n--- Search Student ---")
    student_id = input("Enter student ID to search: ").strip()
    for student in students:
        if student["id"] == student_id:
            print(f"Found: ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
            return
    print("Student not found.")


def delete_student(students):
    """
    Delete a student record by ID.
    Args:
        students (list): List of student records.
    """
    print("\n--- Delete Student ---")
    student_id = input("Enter student ID to delete: ").strip()
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found.")


def get_valid_int(prompt):
    """
    Validate integer input from the user.
    Args:
        prompt (str): Input prompt message.
    Returns:
        int: Valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main_menu():
    """
    Display the main menu and handle user choices.
    """
    students = load_data()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            save_data(students)
            print("Data saved. Exiting program...")
            break
        else:
             print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
