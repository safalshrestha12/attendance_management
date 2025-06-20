from datetime import date

def take_attendence():
    with open("student.txt", "r") as  file:
        students_data= file.readlines()
        student_attendence=[]
        for student in students_data:
            student=student.strip()
            roll=student.split(",")[0]
            name=student.split(",")[1]
            while True:
                print(f"Roll: {roll}, Name: {name}")
                attendence=input("Present (y/n)").lower()
                if attendence == "y" or attendence == "n":
                    student_attendence.append(f"roll,{name},{attendence}\n")
                    break
                else:
                    print("Enter Valid Input")
        with open (f"attendence/{date.today()}.txt","w") as file:
            file.writelines(student_attendence)
           
    print ("You are on take attendence funnction")


import os

def view_attendence():
    date_input = input("Enter date(yyy-dd-mm) to view student")
    if os.path.exists(f"attendence/{date_input}.txt"):
        with open(f"attendence/{date_input}.txt", "r") as file:
            attendence_data = file.readlines()
            for attendence in attendence_data:
                print(attendence.strip())
    else:
        print("File Does not Exist")

