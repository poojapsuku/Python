str1=" Hi,Welcome to Python "
# To Find the Length of the String
print(str1 + "\nLength of string = "+str(len(str1)))

# To print Specified location of String
print(str1[5])

# To print part of a string
print(str1[4:11])
#To print beg of string and spcifid loc
print(str1[:4])
#Negtive Indexing
print("Ngative Indexing :"+str1[-12:-4])

# To check certain word in a string
print("Python" in str1)

""" This is the multiline Comment
Section"""
str2=""" This is the way to assign
multiline string to a variable"""
print(str2)

# To remove white spaces from beginning and end of a string
print(str1.strip())

# Modify strings
print("LOwer case " + str1.lower())
print("Upper Case " + str1.upper())
print("Replace "+str1.replace("P","J"))
print("Split "+ str(str1.split(",")))

#Concatenation

print(str1+" "+str2)
age = 20
mark1 = 97
mark2 = 100
txt = "My name is Anna, and I am {}"
txt1 = "My name is Anna, and I am {} ,I have {} marks on Python and {} maks on Java"
# Method to insert numbers int o string
print(txt.format(age))
print(txt1.format(age,mark1,mark2))
