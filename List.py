values=["PYTHON", "JAVA", "C", "C++"]
print(values)
print(values[1])
values[2]="JAVASCRIPT"
print(values)
print(values[-4])

#Add a List to an another list
values = values + ["Welcome",20]
print(values)

# To add a value to the list
values.append("Ruby")
print(values)

# To add a value to the list by user
#values.append(input("Enter a list value"))
#print(values)
values[1:3]=["XML"]
values.insert(2,"FLASK")
print(values)

db=("SQL","MYSQL","ORACLE")   # tuple value
values.extend(db)
print(values)

# Remove List Items
values.remove("XML")
print(values)

# To Remove Specified Index
values.pop(1)
print(values)

# to remove last item
values.pop()
print(values)

# To Clear the list values
#values.clear()
#print(values)

# To delete entire list
# del values
print(values)

# To Sort list items
#values.sort()
print(values)