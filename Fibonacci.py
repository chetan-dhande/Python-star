Nterms=int(input("How many terms ?"))
n1=0
n2=1
count=0
print("fibonacci sequence upto",Nterms,"!")
while count < Nterms:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    count+=1