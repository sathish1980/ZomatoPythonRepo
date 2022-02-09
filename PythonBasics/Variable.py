class variablename:

    def __init__(self):
        print("This is constructor")
    #function with partameter
    def addition(self,a,b):
       # global a
        try:
            c = int(a) / b
            d=True
            print(c)
            print(type(a))
            print(type(d))
        except Exception:
            print(Exception)
        finally:
            print("This is finally block")

    #Function with out return Type and with Parameter
    def subtraction(self,a):
        b = 20
        b+=20#20+20 # b= b+20
        c = a - b
        print(c)
        d=self.div(a)
        print(d)


    # Function with return Type and with Parameter
    def  div(self, a):
        b = 20
        c = b/a
        print(c)
        return c

    #Function without parameter
    def mul(self,):
        a=20
        b = 20
        c = a - b
        print(c)

    def voter_id(self, age):
        if age>18:

            print("You are eligible")
            if age>50 or age<35 :
                print("you are elgibile for senior citizen")
                if age >75:
                    print("You are eligible for super senior citizen")
        elif age>15:
            if age==16:
                print("you are going to be eligible in 2 years")
            elif age==17:
                print("you are going to be eligible in 1 years")
            else:
                print("You are going to be eligible in 3 years")
        else :
            print("You are not eligible")


    def bookinsystem(self,nooftickets,gender):
        ticketcost=200
        totalpayafterdiscount=0

        if gender=="Male" and nooftickets>=5:
            discount=200*0.1
            print("Your discount amount for per ticket is : "+str(discount))
            totaldiscount=discount*nooftickets
            totalticketcostwithoutdiscount=ticketcost*nooftickets
            print("Your discount amount for total ticket is : " + str(totaldiscount))
            totalpayafterdiscount=totalticketcostwithoutdiscount-totaldiscount
        elif gender=="FeMale" and nooftickets>=5:
            discount = 200 * 0.2
            print("Your discount amount is : " + str(discount))
            totaldiscount = discount * nooftickets
            totalticketcostwithoutdiscount = ticketcost * nooftickets
            totalpayafterdiscount = totalticketcostwithoutdiscount - totaldiscount
        else:
            print("You are not eligible for discount")
            totalticketcostwithoutdiscount = ticketcost * nooftickets
            totalpayafterdiscount = totalticketcostwithoutdiscount

        print("You have to pay : rs . " +str(totalpayafterdiscount) )

    def whileloop(self,fest):

        book=1
        while book<=100:
            print("Your booking is confirmed for " + str(book) +" tickets")
            book=book+1
            if fest=="Yes" and book==50:
                pass

    def forloopconcept(self):

        alphabets=['A','B','C','D','E','F']
        for ca in alphabets:
            print(ca)

        Numbers=[1,3,10,15,25,32,9]
        for te in Numbers:

            if te>=10:
                print(te)
                break

        for rangeexpample in range(5,10):
            print(rangeexpample)
            if rangeexpample==7:
                break
            for innerforloop in range(20):
                print("inner forloope: " + str(innerforloop))





var=variablename()
var.addition(10,0)
var.subtraction(3)
var.voter_id(16)
var.bookinsystem(5,"FeMale")
var.whileloop("Yes")
var.forloopconcept()









