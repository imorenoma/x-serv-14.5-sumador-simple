#!/usr/bin/python3
import sys


def f_sum(num1, num2):

    print("Suma =", float(num1) + float(num2))


def f_rest(num1, num2):
    print("Resta =", float(num1) - float(num2))


def f_multi(num1, num2):
    print("Multiplicacion =", float(num1) * float(num2))


def f_div(num1, num2):
    try:
        print("la division es:", float(num1) / float(num2))

    except ZeroDivisionError:
        print("Error try to divided per zero")


try:

    if sys.argv[2] == '+':
        f_sum(sys.argv[1], sys.argv[3])

    elif sys.argv[2] == '-':
        f_rest(sys.argv[1], sys.argv[3])

    elif sys.argv[2] == 'x' or sys.argv[2] == '*':
        f_multi(sys.argv[1], sys.argv[3])

    elif sys.argv[2] == '/' or sys.argv[2] == '//':
        f_div(sys.argv[1], sys.argv[3])

    else:
        raise ValueError("Fatal Error")

except ValueError:
    print("could not convert string to float:", sys.argv[1], sys.argv[2], sys.argv[3])
except OverflowError as err2:
    print(err2, "OverflowError")
