import re


class Textfile:
    def fileread(self):
        f = open("C:\\Users\\sathishkumar\\PycharmProjects\\WeekdayPython\\inputFile\\input.txt", "r")
        #print(f.read())
        #print(f.read(10))
        #print(f.readline())
       # print(f.readlines())
        iterate=f.readlines()
        for xc in iterate:
            print(xc)
        f.close()

    def filereadfindaword(self,matchstring):
        f = open("C:\\Users\\sathishkumar\\PycharmProjects\\WeekdayPython\\inputFile\\input.txt", "r")
        iterate=f.readlines()
        count=0
        for xc in iterate:
            count+=1
            #print(xc)
            setstore=re.split("\s",xc)
            #print(setstore)
            for eachvalu in setstore:
                #print(eachvalu)
                if (eachvalu==matchstring):
                    print("The given string is "+ matchstring +" identified in line number : "+str(count))

        f.close()


    def writefile(self):
        f = open("C:\\Users\\sathishkumar\\PycharmProjects\\WeekdayPython\\inputFile\\output.txt", "w")
        #print(f.readline())
        print(f.write("This is write content"))
        f.close()

    def readandwrite(self):
        reads = open("C:\\Users\\sathishkumar\\PycharmProjects\\WeekdayPython\\inputFile\\input.txt", "r")
        f = open("C:\\Users\\sathishkumar\\PycharmProjects\\WeekdayPython\\inputFile\\writefile.txt", "w")
        # print(f.readline())
        f1 = reads.readlines()
        for x in f1:
            print(f.write(x))

obj=Textfile()
obj.readandwrite()
