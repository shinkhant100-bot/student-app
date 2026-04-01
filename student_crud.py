import os

FILE_NAME = "student.txt"

def createStudent():
    studentID = input("Enter ID: ")
    studentName = input("Enter Name: ")
    studentAge = input("Enter Age: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{studentID},{studentName},{studentAge}\n")

    print("Student added successfully! \n")

def viewStudents():
    if not os.path.exists(FILE_NAME):
        print("There is not students.\n")
        return
    
    print("\n Student List: ")
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
        if not lines:
            print("No students found.\n")
            return
        for line in lines:
            studentID, studentName, studentAge = line.strip().split(",")
            print(f"ID: {studentID}, Name: {studentName}, Age: {studentAge}")
    print()

def updateStudent():
    if not os.path.exists(FILE_NAME):
        print("No student found.\n")
        return
    
    studentID = input("Enter the ID of student to update: ")
    updated = False
    new_lines = []

    with open(FILE_NAME, "r")as f:
        for line in f:
            sID, sName, sAge = line.strip().split(",")
            if sID == studentID:
                newName = input(f"Enter new name (current: {sName}): ")
                newAge = input(f"Enter new age(current: {sAge}): ")
                new_lines.append(f"{sID}, {newName},{newAge}\n")
                updated = True
            else:
                new_lines.append(line)

    if updated:
        with open(FILE_NAME, "w") as f:
            f.writelines(new_lines)
        print("Student updated successfully\n")
    else:
        print("Student ID not found.\n")


def deleteStudent():
    if not os.path.exists(FILE_NAME):
        print("No students found.\n")
        return
    
    studentID = input("Enter the ID of student to delete: ")
    deleted = False
    new_lines = []

    with open(FILE_NAME, "r") as f:
        for line in f:
            sID, sName, sAge = line.strip().split(",")
            if sID == studentID:
                deleted = True
            else:
                new_lines.append(line)

    if deleted:
        with open(FILE_NAME, "w") as f:
            f.writelines(new_lines)
        print("Student deleted successfully!\n")
    else:
        print("Student ID not found.\n")