import math


def  add(a,b):
    return a+b

def substract(a,b):
    return  a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def sqrt(a):
    result = math.sqrt(a)
    return result

def  sin(a):
    result = math.sin(a)
    return result
def exp(a):
    return a**2

def cos(a):
    result = math.cos(a)
    return result
def tan(a):
    result = math.tan(a)
    return result



print("""

1 - Addition(a,b)
2 - Substraction(a,b)
3 - multiplication(a,b)
4 - division(a,b)
5 - Square(a)
6 - Square root(a)
7 - sin(a)
8 - cos(a)
9 - tan(a)""")
op= int(input('what operation do you want to perform?'))


while op<10:
    if op == 1:
        print("enter the parameters")
        a1= int(input("enter a"))
        b1= int(input("enter b"))
        res1 =add(a1,b1)
        print("addition=", res1)

    elif op == 2:
        a2=int(input("enter a"))
        b2=int(input("enter b"))
        res2 = substract(a2,b2)
        print("substraction=", res2)

    elif op == 3:
        a3=int(input("enter a"))
        a3=int(input("enter b"))
        res3 = multiply(a3,b3)
        print("multiplication=", res3)

    elif op == 4:
        a4=int(input("enter a"))
        b4=int(input("enter b"))
        res4 = divide(a4,b4)
        print("division=", res4)

    elif op == 5:
        a5=int(input("enter a"))
        res5= sqrt(a5)
        print("square root=", a5)

    elif op == 6:
        a6=int(input("enter a"))
        res6 = sin(a6)
        print("sin value=", a6)

    elif op == 7:
        a7=int(input("enter a"))
        res7= exp(a7)
        print("exponential value=", a7)
    elif op == 8:
        a8= int(input("enter a"))
        res8 =cos(a8)
        print("cosine value=",a8)
    elif op == 9:
        a9= int(input("enter a"))
        res9= tan(a9)
        print("tan value=", a9)

    else:

        print('please choose another option')


    new =  int(input("do you want to continue -(Yes - 1),(No - 0)"))
    if new == 1:
        op = int(input("enter operation"))

    elif new == 0:
        print("thanks for using the scientific calculator")
