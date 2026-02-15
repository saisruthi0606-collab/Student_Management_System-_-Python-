import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!\n")

def view_students():
    students = load_students()
    if not students:
        print("No students found.\n")
        return

    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
    print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    students = load_students()

    for s in students:
        if s["roll"] == roll:
            print("Student found:")
            print(s)
            return

    print("Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    students = load_students()

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter new name: ")
            s["age"] = input("Enter new age: ")
            s["course"] = input("Enter new course: ")
            save_students(students)
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    students = load_students()

    new_students = [s for s in students if s["roll"] != roll]

    if len(new_students) == len(students):
        print("Student not found.\n")
    else:
        save_students(new_students)
        print("Student deleted successfully!\n")

def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
