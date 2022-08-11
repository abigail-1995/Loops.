n=int(input("enter num"))
i=1
sum=0
while i<=n:
    print(i**3,"+",end=" ")
    sum=sum+i**3
    i=i+1
    print(sum)
