
b=0

try:
    a=10/b
    print(a)
    print("try completed")
except ZeroDivisionError:
    print("Can't divided by zero")
print("Program completed")