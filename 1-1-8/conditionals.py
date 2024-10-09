
status = True
grades = [67, 95, 88, 42, 99, 77]
def add_grades():
    new_grade = int(input("Enter your new grade: "))
    grades.append(new_grade)
    print("You added the grade " + str(new_grade) + " to your list")
def show_menu():
    for grade in grades:
        print(grade)
def show_grades():
    for grade in grades:
        print(grade)
def delete_grade():
    for grade in grades:
        print(grade)
    delete_grade = int(input("Which index would you like to delete?"))
    if delete_grade == -1:
        print("You deleted the grade: " + str(grades.pop()))
    else:
        print("You deleted the grade: " + str(grades.pop(delete_grade)))

while(status):
    show_menu()
    choice = int(input("Enter your choice: "))
    if choice ==1:
        show_grades()
    elif choice ==2:
        add_grades()
    elif choice ==3:
        print("The following are your grades.  If you wish to simply delete the last one, enter -1")
        show_grades()
        delete_grade()
    elif choice ==4:
        print("You will be completing this part separately")
    elif choice ==5:
        print("Thank you for using our program.  Have a great day!")
        status = False
    else:
        print("Please read the menu carefully and select a valid option.")