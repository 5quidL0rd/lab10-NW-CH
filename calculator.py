#https://github.com/5quidL0rd/lab10-NW-CH
#Partner 1: Blake Fowler
#Partner 2: Grayson Christie 




import math

def square_root(a):
    if a < 0:
        raise ValueError("Must be a positive number")
    return math.sqrt(a)

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def logarithm(a, b):
    if a <= 0:
        raise ValueError("Base must be positive and not equal to 1")
    if b <= 0 or b == 1:
        raise ValueError("Argument must be positive")
    return math.log(a) / math.log(b)

def log(a, b):
    return logarithm(a, b)

def exp(a, b):
    return a ** b

