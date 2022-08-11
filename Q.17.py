num=int(input("enter the number"))
n=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**n
    temp//=10
if num==sum:
    print("armstrong number")
else:
    print("not armstrong number")        