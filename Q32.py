i=1
sum=0
n=int(input("enter num"))
while i<=n:
    if i%2==0:
        print(i*i,end=" ")
    else:
        print("-",i*i,end=" ")
    i=i+1
    sum=sum+1
print(sum)            