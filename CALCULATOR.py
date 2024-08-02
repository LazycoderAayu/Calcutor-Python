i=int(input("enter a number 1 :-"))
e=int(input("enter a number 2 :-"))
p=str(input("enter a opreator   [+ , - ,  * ,  /, ** , // , % ]  "))
if p=="+" :
    print(i+e)
elif p=="-":
    print(i-e)
elif p=="*":
    print(i*e)
elif p=="/":
    print(i/e)
elif p== "**":
    print(i**e)
elif p== "%":
    print(i%e)
elif p== "//":
    print(i//e)
else:
    print('selected opereator is not valid')

