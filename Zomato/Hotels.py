from Zomato.CommonFunctions import CommonFunctions
from Zomato.Menus import Menus


class Hotels(Menus):
    NonVeg={}
    def HotelInfo(self,HotelName,Dish,quantity):
        if(HotelName=="A2B"):
            print(self.VegDish())
        elif(HotelName=="SRV"):
            print(self.VegDish())
        elif(HotelName=="SRR"):
            VegMenu=Menus.VegDish(self)
            print(VegMenu)
            #print(self.NonVegDish())
            NonVeg=Menus.NonVegDish(self)
            print(NonVeg)
        else:
            print("No Hotel Found")
        print("******Welcome to Zomato******")
        print("You have choosen the Dish :" +Dish)
        print("The quantity of the Dish :" + str(quantity))
        vegItemvalus=Menus.VegDishValue(self)
        perPieceAmountValue=vegItemvalus.get(Dish)
        print("Per piece of "+Dish+" is :" + str(perPieceAmountValue))
        TotalAmountwithouttax=Menus.calculationlogic(self,quantity,perPieceAmountValue)
        print(str(quantity)+" piece of " + str(Dish) + " is :" + str(TotalAmountwithouttax))
        taxvalue=Menus.taxcalcultion(self,TotalAmountwithouttax)
        print("Your tax amount is :" + str(taxvalue))
        overallamount=TotalAmountwithouttax+taxvalue
        print("overall billamount of this order is: "+str(overallamount))



    def setIteration(self, iterationvalue):
        for eachValue in iterationvalue:
            print(eachValue)
HT=Hotels()
HT.HotelInfo("SRV","Dosa",5)