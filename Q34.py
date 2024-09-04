# 34.	Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200 ¡ D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500

net_amount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split()
    for i in range(0, len(values), 2):
        operation, amount = values[i], int(values[i+1])
        if operation == 'D':
            net_amount += amount
        elif operation == 'W':
            net_amount -= amount
print(net_amount)
