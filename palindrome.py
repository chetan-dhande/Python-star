no=int(input("Enter the Number:"))
no1=no
rev1=0
while no>0:
    rem=no%10
    rev1=(rev1*10)+rem
    no=no//10
if rev1==no1:
 print("Number is palindrome")
else:
 print("Number is not palindrome")