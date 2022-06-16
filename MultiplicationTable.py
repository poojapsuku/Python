num = int(input("Enter the number to be multiplied::"))
limit=int(input("Enter the limit::"))
print("Multiplication Table of " + str(num) + " is ::")
for x in range(1,limit+1,1):
    #mult= num * x
    print(str(num) + "*" + str(x) + "=" + str(num*x))
