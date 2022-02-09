class Menus:

    veg={"Idly","Dosa","Vada","Poori","MasalDosa"}
    nonveg = {"Biriyani", "egg", "chicken", "mutton", "beef"}
    vegitemvalue={"Idly":8,"Dosa":40,"Vada":10,"Poori":30,"MasalDosa":45}
    def VegDish(self):
        return self.veg
    def NonVegDish(self):
        return self.nonveg
    def VegDishValue(self):
        return self.vegitemvalue
    def calculationlogic(self,NumberofCount,Amount):
        return NumberofCount*Amount

    def taxcalcultion(self,amount):
        return amount*0.07

