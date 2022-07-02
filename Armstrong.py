def armstrong(n):
    temp=n
    sum=0
    while n>0:
        dig=n%10
        sum=sum+dig**3
        n=n//10
    return temp==sum

n=int(input("nter a number::"))
if(armstrong(n)):
    print(str(n) + " is Armstrong number")
else:
    print(str(n) + " is not Armstrong number")