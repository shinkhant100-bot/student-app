from student import createStudent,viewStudents

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


            
        

    