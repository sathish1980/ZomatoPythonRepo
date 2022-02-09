from Inheritance.StrudentAttendance import Studentattendance


class studentacademicinfo(Studentattendance):

    tamil=75
    english=66
    maths=76
    def classTen(self):
        print("Your mark in tamil: "+str(self.tamil))
        print("Your mark in english: " + str(self.english))
        print("Your mark in maths: " + str(self.maths))
    def classNine(self):
        print("Your mark in tamil: "+str(self.tamil))
        print("Your mark in english: " + str(self.english))
        print("Your mark in maths: " + str(self.maths))
    def classEight(self):
        print("Your mark in tamil: "+str(self.tamil))
        print("Your mark in english: " + str(self.english))
        print("Your mark in maths: " + str(self.maths))

obj=studentacademicinfo()
obj.attendancepercentage(5)
obj.persinalloaninterestRate(5,3000)
obj.carloaninterestRate(2,10000)
obj.classTen()