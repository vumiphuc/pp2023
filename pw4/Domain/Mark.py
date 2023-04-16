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