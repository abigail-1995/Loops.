num=int(input("enter num"))
dec=0
p=1
while num!=0:
    rev=num%10
    num=num//10
    dec=dec+rev*p
    p=p*2
print(dec)    