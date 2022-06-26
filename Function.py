"""def add(a, b):
    sum1 = a + b
    return sum1


a = int(input("Enter a Value::"))
b = int(input("Enter b Value::"))
print("Sum of the numbers = " + str(add(a, b)))"""


# Arbitary Argument
def hey(*values):
    print(" da"+values[1])


hey("Pooja","Pooh")

# Return Values
def rtn(x):
    return 10 * x

print(rtn(20))
print(rtn(10))

# Passing a list as an argument

def My_fun(cars):
    for x in cars:
        print(x)

car=["Audi","BMW","Ford","Innova"]
My_fun(car)


# Keyword Argument

def fun(name,age):
    print(name,age)

fun(age=10,name="Pooja")

# dafault argument
def fun(name,age=20):
    print(name,age)

fun(name="Pooja",age=23)

# sum
def sum(num1,num2):
    sum1=num1+num2
    return sum1
print(sum(10,15))