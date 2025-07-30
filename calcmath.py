import math 

import re

num_1=int('1')
num_2=int('2')
num_3=int('3')
num_4=int('4')
num_5=int('5')
num_6=int('6')
num_7=int('7')
num_8=int('8')
num_9=int('9')

def calculate(calcstr):
    calcstr=calcstr.replace(" ","")
    for op in "+-*/":
        if op in calcstr:
            left, right = calcstr.split(op)
            num_1=int(left)
            num_2=int(right)
            if op=="+":
                return num_1+num_2
            elif op == "-":
                return num_1-num_2
            elif op == "*":
                return num_1*num_2
            elif op == "/":
                return num_1/num_2
    return "Invalid input"

def calc(line):
    patt = re.compile('^[0-9]+|[+\-\/*][0-9]+')
    nums = re.findall(patt, line)
    number = int(nums[0])
    for num in nums[1:]:
        if num[0] == "+":
            number = number + int(num[1:])
        elif num[0] == "-":
            number == number - int(num[1:])
        elif num[0] == "*":
            number = number * int(num[1:])
        elif num[0] == "/":
            number == number / int(num[1:])
    return(str(number))
    



