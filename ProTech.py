# Let start afresh
# In the making of a scientific calculator using Tkinter framework
# let get to work oops.........

# WHere do we start from......
# Okay we move

import math


from tkinter import*


def operation():
    # The Executor function
    # Equal to
    global cal
    try:
        action = str(eval(cal))
        Input.set(action)
    except:
        action = cal.split("(")
        if action[1][len(action[1])-1] == ")":
            num = action[1][:-1]
            if action[0] == 'cos':
                a = math.cos(math.radians(float(num)))
                Input.set(a)
            elif action[0] == 'sin':
                a = math.sin(math.radians(float(num)))
                Input.set(a)
            elif action[0] == 'tan':
                a = math.tan(math.radians(float(num)))
                Input.set(a)
            elif action[0] == 'log':
                a = math.log10((float(num)))
                Input.set(a)
        # print("Hello")


def click(num):
    global cal
    cal = cal + str(num)
    Input.set(cal)


def clear():
    global cal
    cal = ""
    Input.set('')


Call = Tk()
Call.title("Scientific Calculator ")
cal = ""
Input = StringVar()

# Background color(bg) = Black
# Foreground color(fg) = white
# The Entry box takes the spaces of two rows(0 to 1) ans also the column takes 4 spaces

entry = Entry(Call, font=("Roman", 18, "bold"), textvariable=Input, bd=30, insertwidth=4, bg="white",
              justify='right').grid(rowspan=2, columnspan=4)

# For the first set of buttons
# Row 2 which includes
# i) Clear button  ii) Bracket buttons

clear_btn = Button(Call, padx=6, pady=6, bd=3, fg='white smoke', font=("Roman", 14, 'bold'), text="C", bg="gray45",
                   command=clear ).grid(row=2, column=0)

bracket_btn1 = Button(Call, padx=6, pady=6, bd=3, fg='white smoke', font=("Roman", 14, "bold"), text="(", bg="gray45",
                      command=lambda: click("(")).grid(row=2, column=2)

bracket_btn2 = Button(Call, padx=6, pady=6, bd=3, fg="white smoke", font=("Roman", 14, 'bold'), text=")", bg='gray45',
                      command=lambda: click(")")).grid(row=2, column=3)

# For the second set of buttons
# Row 3 which includes
# Buttons for number 7, 8, 9 and also the addition button.

seven_btn = Button(Call, padx=6, pady=6, bd=3, font=("Roman", 14, 'bold'), fg="white smoke", text="7", bg="gray45",
                   command=lambda: click(7)).grid(row=3, column=0)

eight_btn = Button(Call, padx=6, pady=6, bd=3, font=("Roman", 14, "bold"), fg="white smoke", text='8', bg= 'gray45',
                   command=lambda: click(8)).grid(row=3, column=1)

nine_btn = Button(Call, padx=6, pady=6, bd=3, font=("Roman", 14, "bold"), fg='white smoke', text="9", bg='gray45',
                  command=lambda: click(9)).grid(row=3, column=2)

add_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='+', bg= 'gray45',
                 command=lambda: click('+')).grid(row=3, column=3)

# For the third det of buttons
# Row 4 which includes
# Buttons for number 4, 5, 6 and also the minus button

four_btn = Button(Call, padx=6, pady=6, bd=3, font=("Roman", 14, "bold"), fg='white smoke', text="4", bg="gray45",
                  command=lambda: click(4)).grid(row=4, column=0)

five_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text="5", bg='gray45',
                  command=lambda: click(5)).grid(row=4, column=1)

six_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text="6", bg='gray45',
                 command=lambda: click(6)).grid(row=4, column=2)

minus_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', '14', 'bold'), fg='white smoke', text='-', bg='gray45',
                   command=lambda: click('-')).grid(row=4, column=3)

# Row 5 which includes
# Buttons for number 1, 2, 3 and also the division button

one_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='1', bg= 'gray45',
                 command=lambda: click(1)).grid(row=5, column=0)

two_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='2', bg= 'gray45',
                 command=lambda: click(2)).grid(row=5, column=1)

three_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='3', bg='gray45',
                   command=lambda: click(3)).grid(row=5, column=2)

div_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='/', bg='gray45',
                 command=lambda: click('/')).grid(row=5, column=3)

# Row 6 which includes
# Buttons for number 0, = sign, . sign, multiplication sign *

zero_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='0', bg='gray45',
                  command=lambda: click(0)).grid(row=6, column=0)

equals_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='=', bg='gray45',
                    command=operation).grid(row=6, column=1)

dot_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='.', bg='gray45',
                 command=lambda: click('.')).grid(row=6, column=2)

Multi_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='*', bg='gray45',
                   command=lambda: click('*')).grid(row=6, column=3)
# Seventh row
# Includes log, cos, sin, tan button

log_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='log', bg='gray45',
                 command=lambda: click('log(')).grid(row=7, column=0)

sin_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='sin', bg='gray45',
                 command=lambda: click('sin(')).grid(row=7, column=1)

cos_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='cos', bg='gray45',
                 command=lambda: click('cos(')).grid(row=7, column=2)

tan_btn = Button(Call, padx=6, pady=6, bd=3, font=('Roman', 14, 'bold'), fg='white smoke', text='tan', bg='gray45',
                 command=lambda: click('tan(')).grid(row=7, column=3)

Call.mainloop()
