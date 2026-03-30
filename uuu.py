
students = []

def createStudent():
    studentID = input("Enter ID : ")
    studentName = input("Enter Name :")
    studentAge = input("Enter Age : ")

    student = {
        "id": studentID,
        "name": studentName,
        "age": studentAge
    }
    students.append(student)
    print("student added successfully\n")


def viewStudents(): 
    if not students:
        print("student are not found\n")
        return

    print("\nstudent list : ")
    for s in students: 
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}")
    print()

while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            createStudent()
        elif choice == "2":
            viewStudents()
        elif choice == "3":
            print("Bye")
            break
        else:
            print("Invalid choice\n")

qewwewe
            
        

    