a=int(input("enter the 1st num"))
b=int(input("enter the 2nd num"))
c=input("enter operation")
if(c=="add"):
    print(a,"+",b,"=",a+b)
elif(c=="sub"):
    print(a,"-",b,"=",a-b)
elif(c=="mul"):
    print(a,"*",b,"=",a*b)
elif(c=="div"):
    print(a,"/",b,"=",a/b)
else:
    print("enter any operators like add,sub,mul,div")
