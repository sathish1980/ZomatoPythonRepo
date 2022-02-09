from Inheritance.Bank import Bankinfo


class Studentattendance(Bankinfo):
    totalworkingdays=250
    totalgovernmentholidays=20
    naturaldisasture=10

    def attendancepercentage(self,totalnoofleaves):
        totalworkingdayforstudent=self.totalworkingdays-totalnoofleaves
        leavepercentage=totalworkingdayforstudent/self.totalworkingdays
        print(leavepercentage*100)




