from Domain.Student import *
from Domain.Course import *
from Domain.Mark import *


list_of_students = []
list_of_courses = []
list_of_marks = []

def input_student():
     num_students = int(input("Enter the number of students in the class: "))
     for i in range(num_students):
        stid = input("Enter student's id: ")
        stname = input("Enter student's name: ")
        stDob = input("Enter student's DOB: ")
        stu = Student(stid, stname, stDob)
        list_of_students.append(stu)
        
def input_course():
     num_courses = int(input("Enter the number of courses: "))
     for i in range(num_courses):
        coid = input("Enter course's id: ")
        coname = input("Enter course's name: ")
        cou = Course(coid, coname )
        list_of_courses.append(cou)
        
def input_mark(list_of_students, list_of_courses, list_of_marks):
     course_id = input("Enter course ID: ")
     course = None
     for i in list_of_courses:
        if i.get_coid() == course_id:
            course = i
            break
     if course is not None:
        for j in list_of_students:
                mark = float(input(f"Enter mark for student {j.get_stid()}: "))
                mark = Mark(course, j, mark)
                list_of_marks.append(mark)
     else:
        print("Invalid course")