#!/usr/bin/python3
import sys


def suma(num1, num2):
    return num1+num2


def resta(num1, num2):
    return num1-num2


def multiplica(num1, num2):
    return num1*num2


def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Error: trying to divided by zero"


operaciones= {"suma": suma, "resta": resta, "multiplica": multiplica, "divide": divide}

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit("Bad number of arguments")

    try:
        operando = sys.argv[1]
        number1 = float(sys.argv[2])
        number2 = float(sys.argv[3])

    except IndexError:
        sys.exit("Usage: operator number1 number2")
    except ValueError:
        sys.exit("num1 & num2 must be integer")

    try:
        result = operaciones[operando](number1, number2)
    except KeyError:
        sys.exit("The operator does not exist")

    print(result)
