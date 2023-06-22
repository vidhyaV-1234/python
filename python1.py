x=int(input("enter the integer" ))
fact=1
if x%2==1:
    for i in range(1,x+1):
        fact=fact*i
    print(fact)
else:
    c=str(x)
    if c[::-1]== str(x):
        print("it is palindrom")
    else:
        print("it is not palindrom")
