n=input("enter number")
l=list(n)
i=0
a=["zero","one","two","three","four","five","six","seven","eight","nine"]
while i<len(l):
    print(a[int(l[i])],end=" ")
    i=i+1