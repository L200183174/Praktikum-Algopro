personalData = {"Name" : "Azie Melasari",
                "NIM" : "L200183174",
                "Address" : "Lemahbang, Karanganyar, Sambungmacan, Sragen",
                "Majors" : "Double Degree of Informatics Engineering",
                "Faculty" : "FKI",
                "Religion" : "Islam",
                "Hobby" : "Swimming"}

def Name():
    print(personalData["Name"])
def NIM():
    print(personalData["NIM"])
def Address():
    print(personalData["Address"])
def Majors():
    print(personalData["Majors"])
def Faculty():
    print(personalData["Faculty"])
def Religion():
    print(personalData["Religion"])
def Hobby():
    print(personalData["Hobby"])

def x() :
    print(""" Available Choice :
-x Display Choice
-1 Display Name
-2 Display NIM
-3 Display Addresss
-4 Display Majors
-5 Display Faculty
-6 Display Religion
-7 Display Hobby
-c Close The Program""")
x()

while True :
    y = input ("Your Choice: ")
    if y == "x":
        x()
    elif y == "1":
        Name()
    elif y == "2":
        NIM()
    elif y == "3":
        Address()
    elif y == "4":
        Majors()
    elif y == "5":
        Faculty()
    elif y == "6":
        Religion()
    elif y == "7":
        Hobby()
    elif y == "c":
        print ("The Program is closed")
        break
    else:
        print("Invalid")
