class Bankinfo:

    P_interestpercentage=0.13
    H_interestpercentage = 0.6
    C_interestpercentage = 0.8
    def persinalloaninterestRate(self,years,amount):
        actualinterest=amount*self.P_interestpercentage
        print("You have to pay interest for one month is "+str(actualinterest))
        print("over all interest is " + str(actualinterest*(years*12)))
    def homeloaninterestRate(self,years,amount):
        actualinterest=amount*self.H_interestpercentage
        print(actualinterest)
    def carloaninterestRate(self,years,amount):
        actualinterest=amount*self.C_interestpercentage
        print(actualinterest)





