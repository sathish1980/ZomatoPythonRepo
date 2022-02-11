import random


class Randoninput:

    def voterid(self):
        #age=random.random() # return the decimal value
        age = random.randint(1,100)  # return the int value with in the range
        print("Your age is : "+ str(age))
        if age>18:
            print("You are eligible to apply voter id")
        else:
            print("You are not elgible to apply voter id")
obj =Randoninput()
obj.voterid()
