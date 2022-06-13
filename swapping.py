# Swapping
a=int(input("Enter Value A :"))
b=int(input("Enter Value B :"))
print("\nBefore Swapping")
print("Value of A = "+str(a) +"\t"+ "Value of B = " + str(b))
temp=a
a=b
b=temp
print("After Swapping")
print("Value of A = "+str(a) + "\t"+ "Value of B = " + str(b))

print("_____________________________________")
print("Swapping using Without temp variable")
print("_____________________________________")
print("Before Swapping")
print("Value of A = "+str(a) +"\t"+ "Value of B = " + str(b))
a=a+b
b=a-b
a=a-b
print("After Swapping")
print("Value of A = "+str(a) + "\t"+ "Value of B = " + str(b))

