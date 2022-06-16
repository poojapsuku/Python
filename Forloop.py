files = ["Pirates of Carribean.mp4", "Joker.mp4", "Life of PI.mp4", "Family Man.mp4"]
for x in files:
    print(x[0:-4])

# To Print individual Letters of the string

word = "Lord Almighty"
for w in word:
    print(w)
# Using the for loop to iterate over a Python list

Program = ["JAVA", "PYTHON", "C", "C++"]
for word in Program:
    print(word)

# Using the for loop to iterate over a Python Tuple
num = (1, 2, 3, 4)
sum_num = 0
for i in num:
    sum_num = sum_num+i
print(f'Result is {sum_num}')

# Nested Loop
lim=int(input("Enter the Limit::"))
k=(2*lim)-2
for i in range(0,lim):
    for j in range(0,k):
     print(end="")
     k=k-1
    for j in range(0,i+1):
        print("*",end="")
    print(" ")