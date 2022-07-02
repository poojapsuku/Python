def isPal(n):
    temp=n
    rev=0
    while n>0:
        dig=n%10
        rev=rev*10+dig
        n=n//10
    return rev==temp

n=int(input("Enter a number::"))
if isPal(n):
    print(str(n) + " is Palindrome")
else:
    print(str(n) + " is not Palindrome")