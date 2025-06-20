def add_student():
    roll_no = input("Enter Your RollNo: ")
    name=input("Enter YOur Name: ")
    contact_no=input("Enter Your Contact No:")
    with open("student.txt","a")as student:
        student.write(f"{roll_no},{name},{contact_no}\n")
    print("Student Record Added succesfuly")


def view_student():
    with open("Student.txt","r") as student_data:
        students = (student_data.readlines())
        for student in students:
            print(student.strip())




def update_student():
    # ask student roll number
    roll_no = input ("Enter Roll No of student you want to update")
    updated_student_record = []
    is_updated = False
    #step1 open file on read mode
    with open("student.txt", "r") as student_data:
        students= student_data.readlines()
        for student in students:
            student_record = student.strip
            student_roll = student_record.split(",")
        # step2 findout if student roll number is present or not
            if student_roll[0] == roll_no:
                print(f"Student Record Found {student_record} ")
                name= input ("Enter Student Name:")
                contact = input ("Enter Student Contact No: ")
                updated_student_record.append(f"{roll_no},{name},{contact}\n")
                is_updated= True
            else:
                updated_student_record.append(student)
        if is_updated:
            with open("student.txt", "w") as file:
                file.writelines(updated_student_record)
                print("Student Record added successfully")
        else:
            print(f"Student with {roll_no} does not exist")

    #step 3 if roll number exist ask user to enter new records
    # step 4 write update records in files

def delete_student():
    print("you are on Delete Student Function")

def view_student():
    print("You are on view student function")

def take_attendence():
    print ("you are on take attendence function")

def view_attendence():
    print ("you are on view attendence function")

def exit_student():
    print ("you are on exit function")