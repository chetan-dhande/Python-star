a=int(input("Enter the first Number :"))
b=int(input("Enter the second Number :"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is :",min1)
        break
    min1=min1+1