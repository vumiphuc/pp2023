from Domain.Student import *
from Domain.Course import *
from Domain.Mark import *
from input import *
from output import *


while True:
    print('Select an option:')
    print('1. Enter student information')
    print('2. Enter course information')
    print('3. Enter mark')
    print('4. List all students')
    print('5. List all courses')
    print('6. Calculate GPA for a students')
    print('7. Sort GPA')
    print('8. List all marks for a course')
    print('9. Exit')
    option = int(input('Enter your option: '))
    if option == 1:
        input_student()
    elif option == 2:
        input_course()
    elif option == 3:
        input_mark(list_of_students,list_of_courses,list_of_marks)
    elif option == 4:
        show_list_of_student()
    elif option == 5:
        show_list_of_course()
    elif option == 6:
        stid = input("Enter student ID: ")
        print(" GPA: " + str(Mark.calculate_gpa(stid)))
    elif option == 7:
        Mark.sort_gpa(list_of_students)
    elif option == 8:
        course_id = input("Enter course ID: ")
        show_marks_for_course(course_id, list_of_marks)
    elif option == 9:
        break