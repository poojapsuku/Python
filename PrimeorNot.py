
def PrimeorNot(num):
    flag = False
    for i in range(2, num):
        if num % i == 0:
            flag = True

    if flag:
        print(str(num) + " is not Prime")
    elif num == 1:
        print(str(num) + " is not Prime")
    else:
        print(str(num) + " is  Prime")

print("Welcome")
print(__name__)  # return module

