# 33.	Write a program which accepts a sequence of comma‐separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
import sys

def generate_list_and_tuple():
    input_str = input("Enter a sequence of comma-separated numbers: ")
    num_list = input_str.split(',')
    num_tuple = tuple(num_list)
    print(num_list)
    print(num_tuple)

if __name__ == "__main__":
    generate_list_and_tuple()
