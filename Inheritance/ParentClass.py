from Inheritance.Bank import Bankinfo
from Inheritance.StrudentAttendance import Studentattendance


class Customerpersonalinfo(Bankinfo,Studentattendance):

    name="sathish"
    age=50
    dob=1990
    address="no 19 ,chennai"
    def baseicinfo(self):
        print("Your name is : "+self.name)
        print("your age is : "+str(self.age))
        print("Your dob is : "+str(self.dob))
        print("Your address is : "+str(self.address))
    def catloaninsterestrate(self):
        print("Your car laon a interest percentage is " +str(self.C_interestpercentage))

cpi=Customerpersonalinfo()
cpi.baseicinfo()
cpi.persinalloaninterestRate(4,5000)
cpi.catloaninsterestrate()
cpi.attendancepercentage(15)