# Write a Python program to take a input from user in a list and print it.
num = int(input("Enter the number of elements in the list: "))
user_list = []
for i in range(num):
    user_list.append(input("Enter element {}: ".format(i+1)))
print("User input list: ", user_list)
