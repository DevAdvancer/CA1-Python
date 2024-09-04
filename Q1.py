# Write a program in Python to find the addition & average of three float numbers
import sys

length = int(input("Enter the Lenght "))
L = [float(input(f"Enter number {i+1}: ")) for i in range(length)]

while True:
    print("1. Addition")
    print("2. Average")
    print("3. Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        add = sum(L)
        print(f"The sum is: {add}")
    elif choice == "2":
        avg = sum(L)/len(L)
        print(f"The average is: {avg}")
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
