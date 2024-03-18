import sys

def add(num1,num2):
    sum=num1 + num2
    return sum

def sub(num1,num2):
    sub=num1 - num2
    return sub

def multiply(num1,num2):
    multiply=num1 * num2
    return multiply

def div(num1,num2):
    div=num1 / num2
    return div

num1=float(sys.argv[1])
operation=sys.argv[2]
num2=float(sys.argv[3])

if operation == "add" :
    print(add(num1,num2))
    
if operation == "sub" :
   print(sub(num1,num2))

if operation == "multiply" :
    print(multiply(num1,num2))

if operation == "div" :
    print(div(num1,num2))