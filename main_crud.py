from student_crud import createStudent, viewStudents, updateStudent, deleteStudent


while True:
    print("=== Student Management ===")
    print("1. Add student")
    print("2. View student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        createStudent()
    elif choice == "2":
        viewStudents()
    elif choice == "3":
        updateStudent()
    elif choice == "4":
        deleteStudent()
    elif choice == "5":
        print("Bye")
        break
    else:
        print("Invalid choice\n")