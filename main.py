from student_management import (
    add_student,update_student,view_student, delete_student,
    )

from attendece_management import (
    take_attendence,view_attendence
)


def menu():
    print("Enter 1 To add student")
    print("Enter 2 To update Student")
    print("Enter 3 To Delete Student")
    print("Enter 4 To View Student")
    print("Enter 5 To Take Attendece")
    print("Enter 6 To View Attendence")
    print("Enter 7 To Exit")
# from student_management import (
#     add_student,update_student,view_student, delete_student, take_attendence,view_attendence
#     )




while True:
    menu()
    option = input("Enter Menu No")

    if option == "1":
        add_student()
    elif option == "2":
        update_student()
    elif option == "3":
        delete_student()
    elif option == "4":
        view_student()
    elif option == "5":
        take_attendence()
    elif option == "6":
        view_attendence()
    elif option == "7":
        print("delete")
    else:
        print("Invalid option")

        
