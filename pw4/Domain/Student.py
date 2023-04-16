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