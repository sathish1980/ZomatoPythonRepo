from Zomato.CommonFunctions import CommonFunctions
from Zomato.Menus import Menus
import pyttsx3


class HotelsusingExcel(Menus):
    NonVeg={}
    # initialize Text-to-speech engine
    engine = pyttsx3.init()
    def HotelInfoExcel(self,HotelName,Dish,quantity):
        if(HotelName=="A2B"):
            self.billing(HotelName,Dish,quantity)
        elif(HotelName=="SRV"):
            self.billing(HotelName, Dish, quantity)
        elif(HotelName=="SRR"):
            self.billing(HotelName,Dish,quantity)
        else:
            print("No Hotel Found")
    def billing(self,HotelName,Dish,quantity):
        print("******Welcome to Zomato******")
        print("You have choosen the Dish :" +Dish)
        print("The quantity of the Dish :" + str(quantity))
        vegItemvalus=Menus.particularHotemMenu(self,HotelName)
        print(vegItemvalus)
        print("The len of the dict is :"+ str(len(vegItemvalus)))
        perPieceAmountValue = vegItemvalus.get(Dish)
        if str(perPieceAmountValue)!="None":
            print("Per piece of " + Dish + " is :" + str(perPieceAmountValue))
            TotalAmountwithouttax = Menus.calculationlogic(self, quantity, perPieceAmountValue)
            print(str(quantity) + " piece of " + str(Dish) + " is :" + str(TotalAmountwithouttax))
            taxvalue = Menus.taxcalcultion(self, TotalAmountwithouttax)
            print("Your tax amount is :" + str(taxvalue))
            overallamount = TotalAmountwithouttax + taxvalue
            print("overall bill amount for this order is: " + str(overallamount))
            self.engine.say("overall bill amount for this order is: " + str(overallamount))
            # play the speech
            self.engine.runAndWait()
        else:
            print("Please try with some other order since its not available at the moment")





    def setIteration(self, iterationvalue):
        for eachValue in iterationvalue:
            print(eachValue)
HT=HotelsusingExcel()
HT.HotelInfoExcel("SRV","Poori",5)