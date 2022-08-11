num=int(input("enter number"))
i=num
rev=0
while i>0:
    b=i%10
    i=i//10
    rev=rev*10+b
    print(rev)
if num==rev:
    print("palindrome number")
else:
    print("not palindrome number")    

