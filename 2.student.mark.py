class Student:
    listStudents = []
    def input_student_information(self):
        print("Add Student")
        infor = {'Stuid' : '','Stuname' : '','DoB' : ''}
        print("Enter ID:")
        infor['Stuid'] = input()
        print("Enter name:")
        infor['Stuname'] = input()
        print("Enter date of birth")
        infor['DoB'] = input()
        self.listStudents.append(infor)
    def show_list_of_student(self):
        for i in range(0, len(self.listStudents)):
            print("ID: ",self.listStudents[i]['Stuid'], " ,Name: ",self.listStudents[i]['Stuname']," ,DoB: ",self.listStudents[i]['DoB'])
            
class Course:
    listCourses = []
    def input_course_information(self):
        print("Add Course")
        infor = {'Couid' : '','Couname' : ''}
        print("Enter ID:")
        infor['Couid'] = input()
        print("Enter name:")
        infor['Couname'] = input()
        self.listCourses.append(infor)
    def show_list_of_course(self):
        for i in range(0, len(self.listCourses)):
            print("ID: ",self.listCourses[i]['Couid'], " ,Name: ",self.listCourses[i]['Couname'])
            
class Mark(Student, Course):
    listMarks = []
    def input_mark(self):
            print("Add Mark")
            infor = {'Couid: ': '','Stuname': '', 'mark' : ''}
            print("Enter student name:")
            infor['Stuname'] = input()
            print("Enter course id:")
            infor['Couid'] = input()
            print("Enter mark:")
            infor['mark'] = input()
            self.listMarks.append(infor)
    def show_list_of_mark(self):
        for i in range(0, len(self.listMarks)):
            print("CouID: ",self.listMarks[i]['Couid'], " ,StuName: ",self.listMarks[i]['Stuname']," ,Mark: ",self.listMarks[i]['mark'])
            
s = Student()
c = Course()
m = Mark()
 
while True:
    print("Your choice:")
    print("1: Enter student")
    print("2: Show list of student")
    print("3: Enter course")
    print("4: Show list of course")
    print("5: Enter mark")
    print("6: Show list of mark")
    print("7: Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        s.input_student_information()
    elif choice == 2:
        s.show_list_of_student()
    elif choice == 3:
        c.input_course_information()
    elif choice == 4:
        c.show_list_of_course()
    elif choice == 5:
        m.input_mark()
    elif choice == 6:
        m.show_list_of_mark()
    elif choice == 7:
        break
    