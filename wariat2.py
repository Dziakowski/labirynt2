import math

def add(a, b) :
    return a + b

def sub(a, b) :
    return a - b

def mul(a, b) :
    return a * b

def div(a, b) :
    return a / b

def pow(a, b) :
    return a ** b

#def sqrt(a) :
    #return math.sqrt (a)

def readint() :
    converted = False
    userNumbers = 0
    while not converted :
        try :
            userNumbers = float (input())
            converted = True

        except ValueError :
            print ('This is not a number')
    return userNumbers

def main() : 

    print (readint())



#code snippet
if __name__ == "__main__":
    main()
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    return a/b

def mult(a, b):
    return a*b

def power(a, b):
    return a**b

def sqrt(a):
    return a ** 0.5

def read_int(): # will only take whole numbers not decimals
    user_input = input('please enter a number ')
    while not user_input.isdigit():  # code validator
        user_input = input('please enter a number ')
    
    if user_input.isdigit():
        return float(user_input)

def read_float(): # better because it accepts wholenumbers 
    converted = False
    while not converted:
        try:
            user_number = float(input('please enter a number '))
            converted = True
        except ValueError :
            print('this is not a number')
    return user_number

def is_correct_sign(sign):
    if sign == "+" :
        return True
    if sign == "*" :
        return True
    if sign == "/" :
        return True
    if sign == "-" :
        return True
    if sign == "-" or sign == "**" :
        return True
    return False


def read_sign():
    ## + - * /  we shall check for these symbols 
    user_sign = input('please enter a mathematical sign ')
    while not is_correct_sign(user_sign):
        user_sign = input('enter a correct mathematical sign')
    return user_sign

def calculate(a, b, sign):
    if sign == "+":
        return add(a, b)
    if sign == "-":
        return sub(a, b)
    if sign == "*":
        return mult(a, b)
    if sign == "/":
        return div(a, b)
    if sign == "**" or "^":
        return power(a, b)

def display(result, sign, num1, num2):
    print(f'{num1} {sign} {num2} = {result}')


def main():
    print('hello, this is a calculator by progbasics students')
    num1 = read_float()
    sign = read_sign()
    num2 = read_float()
    result = calculate(num1, num2, sign)
    display(result, sign, num1, num2)



if __name__ == "__main__":
    main() 
Python 
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    return a/b

def mult(a, b):
    return a*b

def power(a, b):
    return a**b

def sqrt(a):
    return a ** 0.5

def read_int(): # will only take whole numbers not decimals
    user_input = input('please enter a number ')
    while not user_input.isdigit():  # code validator
        user_input = input('please enter a number ')
    
    if user_input.isdigit():
        return float(user_input)

def read_float(): # better because it accepts wholenumbers 
    converted = False
    while not converted:
        try:
            user_number = float(input('please enter a number '))
            converted = True
        except ValueError :
            print('this is not a number')
    return user_number

def is_correct_sign(sign):
    if sign == "+" :
        return True
    if sign == "*" :
        return True
    if sign == "/" :
        return True
    if sign == "-" :
        return True
    if sign == "-" or sign == "**" :
        return True
    return False


def read_sign():
    ## + - * /  we shall check for these symbols 
    user_sign = input('please enter a mathematical sign ')
    while not is_correct_sign(user_sign):
        user_sign = input('enter a correct mathematical sign')
    return user_sign

def calculate(a, b, sign):
    if sign == "+":
        return add(a, b)
    if sign == "-":
        return sub(a, b)
    if sign == "*":
        return mult(a, b)
    if sign == "/":
        return div(a, b)
    if sign == "**" or "^":
        return power(a, b)

def display(result, sign, num1, num2):
    print(f'{num1} {sign} {num2} = {result}')


def main():
    print('hello, this is a calculator by progbasics students')
    num1 = read_float()
    sign = read_sign()
    num2 = read_float()
    result = calculate(num1, num2, sign)
    display(result, sign, num1, num2)



if __name__ == "__main__":
    main()