import math

print("welcome to my simple project")

class calc:

    def sum(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mlt(x, y):
        return x * y

    def dev(x, y):
        return x / y

    def sqx(x):
        return math.sqrt(x)

    def sqy(y):
        return math.sqrt(y)

    def exp(x, y):
        return x ** y


while True:
    try:
        print("-" * 50)
        x = int(input("what is the value of x?: "))
        break
    except:
        print("the value of x isn't valid")


while True:
    try:
        print("-" * 50)
        y = int(input("what is the value of y?: "))
        break
    except:
        print("the value of y isn't valid")


list_operations = ["+", "-", "x", "^", "/", "sqrt_of_x", "sqrt_of_y"]

print("-" * 50)
print(list_operations)
print("-" * 50)


while True:
    try:
        a = input("what operation do you want to use?: ")
        break

    except:
        print("the operation isn't valid")


r = {

    (a == '+'): calc.sum(x ,y),

    (a == '-'): calc.sub(x, y),

    (a == '^'): calc.exp(x, y),

    (a == 'x'): calc.mlt(x, y),

    (a == '/'): calc.dev(x, y),

    (a == 'sqrt_x'): calc.sqx(x),

    (a == 'sqrt_y'): calc.sqy(y)
    
}


print("-" * 50)
print("your answer is:")
print("-" * 50)
print(r)