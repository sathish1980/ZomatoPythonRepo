import re

from PythonBasics.ExcelRead import ExcelRead
from PythonBasics.ExcelreadforZomato import ExcelReadForZomato


class Menus(ExcelReadForZomato):

    veg={"Idly","Dosa","Vada","Poori","MasalDosa"}
    nonveg = {"Biriyani", "egg", "chicken", "mutton", "beef"}
    vegitemvalue={"Idly":8,"Dosa":40,"Vada":10,"Poori":30,"MasalDosa":45}
    EachMenus={}
    menuList={}
    def VegDish(self):
        return self.veg
    def NonVegDish(self):
        return self.nonveg
    def VegDishValue(self):
        return self.vegitemvalue
    def calculationlogic(self,NumberofCount,Amount):
        return int(NumberofCount)*float(Amount)
    def taxcalcultion(self,amount):
        return amount*0.07
    def excelvalue(self):
        EachMenus=ExcelRead.fileread(self,"Veg")
        print(EachMenus)
    def maxuserdRow(self):
        mxRow=ExcelRead.filereadmaxrow(self,"Veg")
    def particularHotemMenu(self,HotelName):
        #HotelName="SRV"
        print("******** Welcome to " +str(HotelName) + "***********")
        EachMenus = ExcelReadForZomato.filereadforZomato(self, "Veg",HotelName)
        mxRow = ExcelReadForZomato.filereadmaxrow(self, "Veg")
        #print(mxRow)
        for eachRow in range(1,mxRow):
            #print(EachMenus.get(HotelName+str(eachRow)))
            eachlistvalue=EachMenus.get(HotelName+str(eachRow))
            splitvalue=re.split("-",eachlistvalue)
            #print("this is split value:"+str(splitvalue))
            self.menuList[splitvalue[0]]=splitvalue[1]
        return self.menuList







