#input student's information
students = {}


def input_students_informations():
    number_of_student = int(input("Enter the number of student in the class:"))
    for i in range (number_of_student):
        student_id = (input("Enter id of student:"))
        student_name = (input("Enter name of student:"))
        student_DoB = (input("Enter DoB of student:"))
        students[student_id] = {"Name" : student_name, "Date of birth" : student_DoB}

#input course's information
courses ={}


def input_courses_informations():
    number_of_course = int(input("Enter the number of course:"))
    for i in range (number_of_course):
     course_id = input("Enter id of course:")
     course_name = input("Enter name of course:")
     courses[course_id] = {"Name" : course_name}

#input student's mark
marks = {}

def input_student_marks():
    course_id = input("Enter course id:")
    if course_id not in courses:
        print("Invalid course")
        return
    for student_id in students:
        mark = float(input(f"Enter the mark for {students[student_id]['Name']}:"))
        if student_id not in marks:
         marks[student_id] = {}
        marks[student_id][course_id] = mark

#student marks
def show_student_mark():
    course_id = input("Enter course id:")
    if course_id not in courses:
        print("Invalid course")
        return
    for student_id in students:
        if student_id in marks and course_id in marks[student_id]:
            print(f"{students[student_id]['Name']}: {marks[student_id][course_id]}")
        else:
            print(f"{students[student_id]['Name']}: Not found")
            
#list students
def list_students():
    for student_id in students:
     print(f"{student_id} : {students[student_id]['Name']}")

#list courses    
def list_courses():
    for course_id in courses:
     print(f"{course_id} : {courses[course_id]['Name']}")
    
            


#Test function
input_students_informations()
input_courses_informations()

while True:
    print("Select your option:")
    print("1. Input marks for a course")
    print("2. List students")
    print("3. List courses")
    print("4. Show students mark")
    print("5. Quit")
    choice = input("Your choice:")
    if choice == "1":
        input_student_marks()
    elif choice == "2":
        list_students()
    elif choice == "3":
        list_courses()
    elif choice == "4":
        show_student_mark()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
      
        
    





        