def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b!=0 else "Cannot divide by zero"

a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Enter op (+,-,*,/): ")

if op == '+': print(add(a,b))
elif op == '-': print(sub(a,b))
elif op == '*': print(mul(a,b))
elif op == '/': print(div(a,b))