num=int(input("Enter the value :"))
temp=num
sum=0
while temp>0:
    rem=temp%10
    sum=sum+(rem**3)
    temp=temp//10
if num==sum:
 print("Armstrong number")
else :
 print("not Armstrong number")