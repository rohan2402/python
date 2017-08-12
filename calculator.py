def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x/y)
print ("1.addition")
print ("2.subtraction")
print ("3.multiply")
print ("4.divide")
choice=int(input("enter choice"))
a=int(input("enter the 1st no"))
b=int(input("enter the 2nd no"))
if choice==1:
    print (add(a,b))
elif choice==2:
    print (subtract(a,b))
elif choice==3:
    print (multiply(a,b))
elif choice==4:
    print (divide(a,b))
else:
   print ("wrong choice")
