
import csv
import os

FILE_NAME = "student.csv"

print(os.path.exists(FILE_NAME))


def load_student():
    student = {}

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                roll_no = int(row["roll_no"])

                student[roll_no] = {
                    "name": row["name"],
                    "marks": int(row["marks"])
                }

    except FileNotFoundError:
        pass

    return student


def save_students(student):
    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = ["roll_no", "name", "marks"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for roll_no, details in student.items():
            writer.writerow({
                "roll_no": roll_no,
                "name": details["name"],
                "marks": details["marks"]
            })


def add_student(name, student, roll_no, marks):

    if roll_no in student:
        raise ValueError("Student already exists")

    student[roll_no] = {
        "name": name,
        "marks": marks
    }

    save_students(student)

    print("Student added successfully!")


def delete_student(student, roll_no):

    if roll_no not in student:
        raise ValueError("Student not found")

    del student[roll_no]

    save_students(student)

    print("Student deleted successfully!")


def search_student(student, roll_no):

    if roll_no in student:
        print("Name:", student[roll_no]["name"])
        print("Marks:", student[roll_no]["marks"])

    else:
        print("Student not found")


# Load existing students from CSV
student = load_student()


while True:

    try:

        print("\nSTUDENT MANAGEMENT SYSTEM")
        print("-------------------------")
        print("1. Add student")
        print("2. Search student")
        print("3. Delete student")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            name = input("Enter name: ")
            roll_no = int(input("Enter roll no.: "))
            marks = int(input("Enter marks: "))

            add_student(name, student, roll_no, marks)

        elif choice == 2:

            roll_no = int(input("Enter roll no.: "))

            search_student(student, roll_no)

        elif choice == 3:

            roll_no = int(input("Enter roll no.: "))

            delete_student(student, roll_no)

        elif choice == 4:

            print("Thank you")
            break

        else:

            raise ValueError("Invalid choice")

    except ValueError as e:

        print(e)

