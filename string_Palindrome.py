def strPal(s):

   return s==s[::-1]

s=input("Enter a String::")
#strPal(s)
if strPal(s):
    print(s+" is Palindrome" )
else:
   print(s+" is not Palindrome "+s[::-1])


print(10 ** 3)
print(121//10)