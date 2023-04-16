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