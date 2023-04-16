from Domain.Student import *
from Domain.Course import *
from Domain.Mark import *
from input import *


list_of_gpa= []

def show_list_of_student():
     for i in list_of_students:
        i.list_students()

def show_list_of_course():
     for c in list_of_courses:
        c.list_courses()
        
def calculate_gpa(stid):  
        mark = 0
        cnt = 0
        for marks in list_of_marks:
            if marks.get_student().get_stid() == stid:
                mark += marks.get_mark()
                cnt += 1
        return Mark.round_down(mark / cnt, 1)
    
def sort_gpa(list_of_students):
        for student in list_of_students:
            GPA = Mark.calculate_gpa(student.get_stid())
            list_of_gpa.append(GPA)
        list_of_gpa.sort(reverse = True)
        for gpa in list_of_gpa:
            for student in list_of_students:
                if gpa == Mark.calculate_gpa(student.get_stid()):
                    print(student.get_stid(), "\t", str(gpa))

def show_marks_for_course(course_id, list_of_marks):
     for m in list_of_marks:
        if m.get_course().get_coid() == course_id:
            print(f"Student ID: {m.get_student().get_stid()}, Mark: {m.get_mark()}")