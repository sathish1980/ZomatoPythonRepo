import re
class strinfconcepts:

    def stringhandle(self):
        name="sathish's"
        lname='kumar'
        multilinestring= """ sathish
        kumar
        r"""
        a=" hello,world and Welcome to besant Technologies "
        print(name)
        print(lname)
        print(multilinestring)
        print(a[1])
        print(len(a))
        for g in a:
            print(g)
        exist= "besant" not in a
        if("besant" in a):
            print("besant is present in the string")
        print(exist)
        transaction="IDFC0012456"
        firstfour=transaction[0:4]
        print(firstfour)
        if(firstfour=="HDFC"):
            print("Yes it has started with HDFC keyword")
        else:
            print("it does not starts with HDFC")

        print(a.upper())
        print(a.lower())
        print(a.strip())
        print(a.lstrip())
        print(a.rstrip())
        afterreplace=a.replace('z','WORLD')
        print(afterreplace)
        print(a.split(" "))
        aftersplit=a.split(" ")
        print(aftersplit[1])
        print(a+name)
        escape="sathish's \"kumar\""
        print(escape)
        print(a.startswith(" hello"))
        print(a.endswith(" "))
        print(a.find("besant"))
        mylist=["playing football","cricket","tennis","baseball"]
        latestlist=["selenium","BDD"]
        print(mylist)
        print(mylist[-2])
        print(len(mylist))
        for onevar in mylist:
            if(onevar=="cricket"):
                print("Yes cricket is avaible in the list")
                break
        totallen=len(mylist)
        for indexing in range(0,totallen):
            print(mylist[indexing])

       # mylist[1:3]=["table Tennis","shuttle","Hockey"]
        print(mylist)
        mylist.insert(2,"Hurdels")
        mylist.insert(2, "cricket")
        print(mylist)
        mylist.append("100 meters")
        print(mylist)
        mylist.extend(latestlist)
        print(mylist)
        mylist.remove("100 meters")
        print(mylist)
        mylist.pop(4)
        print(mylist)
        latestlist.clear()
        print(latestlist)
        i=0
        while i < len(mylist):
            print(mylist[i])
            i=i+1
        mylist.sort()
        mylist.sort(reverse=True)
        print(mylist)
        latestlist=mylist.copy()
        print(latestlist)

        ## Tuple

        books=("sceince","Maths","english")
        standars=(1,2,3)
        print(books)
        print(len(books))
        print(books[1])

        for eachvalue in books:
            #print(eachvalue)
            if eachvalue=="sceince":
                print(eachvalue)
                break
        for sizevale in range(0,len(books)):
            print(books[sizevale])
        print(type(books))
        print(books[-1])
        print(list(books))
        newList=list(books)
        print(type(newList))
        newList.insert(3,"Geography")
        newList.insert(4, "english")
        print(newList)
        books1=tuple(newList)
        print(books1)
        education=books+standars
        print(education)

        i = 0
        while i < len(education):
            print(education[i])
            i = i + 1

        ##set
        fruits={"apple","Mango","Banana","apple"}
        print(fruits)
        print(type(fruits))
        print(len(fruits))
        for eachval in fruits:
            print(eachval)

        fruits.add("jackfriuts")
        fruits.add("apple")
        newlist=list(fruits)
        print(newlist)
        newlist.append("jackfriuts")
        print(newlist)
        #fruits.remove("jackfriuts")
        print(fruits)

        vegdish={"Idly":8,"Dosa":40,"Vada":10,"Poori":30,"MasalDosa":80,"dosaitems":["minidosa","oniondosa","plaindosa'"]}
        print(vegdish)
        print(vegdish["Poori"])
        print(len(vegdish))
        print(vegdish.get("Poori"))
        keyValues=vegdish.keys()
        for eachvalue in keyValues:
            if eachvalue =="Dosa":
                print(vegdish.get(eachvalue))
        print(vegdish.values())

        oneVaraialbe=vegdish.items()
        print(oneVaraialbe)

        if "Dosa" in vegdish:
            print("Yes")
        else:
            print("No")
#update the values
        vegdish["Dosa"]=60
        vegdish.update({"Dosa1":55})
        print(vegdish)

        name="sathish kumar R"
        splitstring=name.split("a")
        print(splitstring)
        for s in splitstring:
            print(s)

        print( re.findall("\s",name))
        print(re.findall("R$",name))















sc = strinfconcepts();
sc.stringhandle()
