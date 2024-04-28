# Define a function to add a student to the system
def add_student(students):
    roll_number = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    student = {'roll_number': roll_number, 'name': name, 'age': age}
    students.append(student)
    print("Student added successfully!")

# Define a function to display all students in the system
def display_students(students):
    if not students:
        print("No students found.")
    else:
        print("List of students:")
        for student in students:
            print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Age: {student['age']}")

# Define a function to search for a student by roll number
def search_student(students):
    roll_number = int(input("Enter Roll Number to search: "))
    found = False
    for student in students:
        if student['roll_number'] == roll_number:
            print(f"Roll Number: {student['roll_number']}, Name: {student['name']}, Age: {student['age']}")
            found = True
            break
    if not found:
        print("Student not found.")

# Define the main function to run the student management system
def main():
    students = []

    while True:
        print("\nStudent Management System Menu:")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
