print("Welcome in Uber")

name =str(input("Enter your  name: "))

print("Welcome",name)

where =(input("Where are you go: "))

mill =int(input("Enter millage: "))

cost = mill*3-1/4*2/6*100-11+15-80*40/2

print("cost= ",cost)

discount =str(input("Are you have discount code: "))

code1 = "mk210"
code2 = "mm"
code3 = "jk"
code4 = "2010"

if discount == "yes" :
    codeI = (input("Enter code:"))
    if codeI == code1 or code2 or code3 or code4:
        dis = cost/2
        print("you have discount %50")
        print(dis)
    else:
        print("it is false code")
else:
    print("ok")