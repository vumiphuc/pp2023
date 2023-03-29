import math

list_of_students = []
list_of_courses = []
list_of_marks = []
list_of_gpa= []

class Student():
    def __init__(self, stid, stname, stDOB):
        self.__stid = stid
        self.__stname = stname
        self.__stDOB = stDOB
    def get_stid(self):
        return self.__stid
    def get_stname(self):
        return self.__stname
    def get_stDOB(self):
        return self.__stDOB
    def list_students(self):
        sid = self.__stid
        sname = self.__stname
        sDob = self.__stDOB
        print('ID:',sid , ', Name:',sname, ', DOB:',sDob)
def input_student():
     num_students = int(input("Enter the number of students in the class: "))
     for i in range(num_students):
        stid = input("Enter student's id: ")
        stname = input("Enter student's name: ")
        stDob = input("Enter student's DOB: ")
        stu = Student(stid, stname, stDob)
        list_of_students.append(stu)
def show_list_of_student():
     for i in list_of_students:
        i.list_students()
        
class Course():
    def __init__(self, coid, coname):
        self.__coid = coid
        self.__coname = coname
    def get_coid(self):
        return self.__coid
    def get_coname(self):
        return self.__coname
    def list_courses(self):
        cid = self.__coid
        cname = self.__coname
        print('ID:',cid , ', Name:',cname)
        
def show_list_of_course():
     for c in list_of_courses:
        c.list_courses()
def input_course():
     num_courses = int(input("Enter the number of courses: "))
     for i in range(num_courses):
        coid = input("Enter course's id: ")
        coname = input("Enter course's name: ")
        cou = Course(coid, coname )
        list_of_courses.append(cou)
        
class Mark():
    def __init__(self,course,student,mark):
        self.__course = course
        self.__student = student
        self.__mark = mark
    def get_course(self):
        return self.__course
    def get_student(self):
        return self.__student
    def get_mark(self):
        return self.__mark
    def round_down(a, decimal=0):
        multiplier = 10 ** decimal
        return math.floor(a * multiplier) / multiplier
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
def show_marks_for_course(course_id, list_of_marks):
     for m in list_of_marks:
        if m.get_course().get_coid() == course_id:
            print(f"Student ID: {m.get_student().get_stid()}, Mark: {m.get_mark()}")
class GPA():
    def __init__(self,stid,gpa):
        self.__stid = stid
        self.__gpa = gpa

    def get_stid(self):
        return self.__stid
    def get_gpa(self):
        return self.__gpa
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