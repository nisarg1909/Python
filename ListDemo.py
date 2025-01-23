studentList = []
studentTitle = ["RollNo","Name","Maths","Science","English"]

for index in range(3):
    student = []
    for title in studentTitle:
        if title == "Name":
            name = input("Enter your name: ")
            student.append(name)
        elif title == "RollNo":
            rollno = int(input("Enter your roll no: "))
            student.append(rollno)
        else:
            marks = int(input(f"Enter your {title} marks: "))
            while marks<0 or marks>100:
                marks = int(input(f"Enter your {title} marks: "))

            student.append(marks)
    print()
    studentList.append(student)

for student in studentList:
    for t,s in zip(studentTitle, student):
        print(f"{t}: {s}")

    print("================================")