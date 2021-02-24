# Sophia M. Toliver, CIS 345 TTH 10:30, A6

from tkinter import *
# from tkinter import ttk
import math

window = Tk()
window.title("Sophia's Calculator")
window.geometry('255x390')
window['bg'] = 'sky blue'

# Global Variables
equation = StringVar()
# formula is a string of an equation that uses eval() to determine the answer of what was inputted
formula = ''


def button_pressed(num):
    """Creates an equation out of what is in the formula box"""
    global formula
    # disable decimal button so user cannot put multiple decimal points in one number
    operators = ['-', '+', '*', '/']
    for symbol in operators:
        if str(num) == symbol:
            decimal_button['state'] = NORMAL
            break
    if str(num) == '.':
        decimal_button.config(state=DISABLED)
    formula += str(num)
    equation.set(formula)


def pos_neg():
    """Convert a negative number to a positive number or vice versus"""
    decimal_button['state'] = NORMAL
    global formula
    # if statements used for exception handling
    if formula == '':
        equation.set('Error')
    else:
        non_number = ''
        operators = ['-', '+', '*', '/']
        for symbol in operators:
            if symbol in formula:
                non_number = 'true'
                equation.set('Error')
                break
            else:
                non_number = 'false'
        if non_number == 'false':
            if float(equation.get()) < 0:
                equation.set(f'{abs(float(equation.get()))}')
            else:
                formula = '-' + formula
                equation.set(f'{formula}')


def clear():
    """Clears what is in the formula box"""
    decimal_button['state'] = NORMAL
    global formula
    formula = ''
    equation.set(formula)


def sqrt():
    """Find the square root of the number entered"""
    decimal_button['state'] = NORMAL
    global formula
    # if statements used for exception handling
    if formula == '':
        equation.set('Error')
    else:
        non_number = ''
        operators = ['-', '+', '*', '/']
        for symbol in operators:
            if symbol in formula:
                non_number = 'true'
                equation.set('Error')
                break
            else:
                non_number = 'false'
        if non_number == 'false':
            square = math.sqrt(float(equation.get()))
            equation.set(f'{square}')


def evaluate():
    global formula
    try:
        if '.' in formula:
            answer = float(eval(formula))
        else:
            answer = int(eval(formula))
        equation.set(str(answer))
        formula = str(answer)
    except (ZeroDivisionError, SyntaxError):
        equation.set('Error')


# Input Equation
input_formula = Entry(window, textvariable=equation, borderwidth=3)
# Allow users to enter numbers ONLY using buttons
input_formula.bind('<Key>', lambda x: 'break')
input_formula.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipadx=10, ipady=10)

# Row 1
decimal_button = Button(window, text='.', fg='blue', command=lambda: button_pressed('.'),
                        height=2, width=5)
decimal_button.grid(row=2, column=0)
sqrt_button = Button(window, text='Sqrt()', fg='blue', command=sqrt, height=2, width=5)
sqrt_button.grid(row=2, column=1)
pos_neg_button = Button(window, text='+-', fg='blue', command=pos_neg, height=2, width=5)
pos_neg_button.grid(row=2, column=2)
clear_button = Button(window, text='Clear', fg='blue', command=clear,
                      height=2, width=5)
clear_button.grid(row=2, column=3)

# Empty label for spacing between buttons
Label(window, text='', bg='sky blue').grid(row=3, columnspan=4)

# Row 2
one = Button(window, text='1', fg='blue', command=lambda: button_pressed(1), height=2, width=5)
one.grid(row=4, column=0)
two = Button(window, text='2', fg='blue', command=lambda: button_pressed(2), height=2, width=5)
two.grid(row=4, column=1)
three = Button(window, text='3', fg='blue', command=lambda: button_pressed(3), height=2, width=5)
three.grid(row=4, column=2)
add_button = Button(window, text='+', fg='blue', command=lambda: button_pressed('+'),
                    height=2, width=5)
add_button.grid(row=4, column=3)

Label(window, text='', bg='sky blue').grid(row=5, columnspan=4)
# Row 3
four = Button(window, text='4', fg='blue', command=lambda: button_pressed(4), height=2, width=5)
four.grid(row=6, column=0)
five = Button(window, text='5', fg='blue', command=lambda: button_pressed(5), height=2, width=5)
five.grid(row=6, column=1)
six = Button(window, text='6', fg='blue', command=lambda: button_pressed(6), height=2, width=5)
six.grid(row=6, column=2)
subtract_button = Button(window, text='-', fg='blue', command=lambda: button_pressed('-'),
                         height=2, width=5)
subtract_button.grid(row=6, column=3)

Label(window, text='', bg='sky blue').grid(row=7, columnspan=4)
# Row 4
seven = Button(window, text='7', fg='blue', command=lambda: button_pressed(7), height=2, width=5)
seven.grid(row=8, column=0)
eight = Button(window, text='8', fg='blue', command=lambda: button_pressed(8), height=2, width=5)
eight.grid(row=8, column=1)
nine = Button(window, text='9', fg='blue', command=lambda: button_pressed(9), height=2, width=5)
nine.grid(row=8, column=2)
multiply_button = Button(window, text='*', fg='blue', command=lambda: button_pressed('*'),
                         height=2, width=5)
multiply_button.grid(row=8, column=3)

Label(window, text='', bg='sky blue').grid(row=9, columnspan=4)
zero = Button(window, text='0', fg='blue', command=lambda: button_pressed(0), height=2, width=5)
zero.grid(row=10, column=2)
equal = Button(window, text='=', fg='blue', command=evaluate, height=2,
               width=11)
equal.grid(row=10, column=0, columnspan=2)
divide_button = Button(window, text='/', fg='blue', command=lambda: button_pressed('/'),
                       height=2, width=5)
divide_button.grid(row=10, column=3)

# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# row_nums = [4, 4, 4, 5, 6, 6, 6, 7, 8, 8, 8, 9, 10]
# i = 0
# j = 0
# for buttons in numbers:
#     button = Button(window, text=buttons, fg='blue', bg='sky blue', bd=0,
#                     command=lambda: button_pressed(int(buttons), equation), height=2, width=5)
#     button.grid(row=row_nums[j], column=i)
#     if i == 2:
#         j += 1
#         Label(window, text='', bg='sky blue').grid(row=row_nums[j], columnspan=4)
#         i = 0
#         j += 1
#     else:
#         i += 1
#         j += 1

window.mainloop()
