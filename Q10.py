# Take input from user if it is greater than 15 print two times of difference if it’s less than 15 print four times of difference.
num = int(input("Enter a number: "))
difference = abs(num - 15)
if num > 15:
    print(2 * difference)
else:
    print(4 * difference)
