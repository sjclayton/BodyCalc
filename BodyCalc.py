from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import math
import os

mainWindow = Tk()

mainWindow.title('BodyCalc')
mainWindow.configure(background='#333')
mainWindow.resizable(False, False)
mainWindow.minsize(390, 260)

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
elif __file__:
    application_path = os.path.dirname(__file__)

iconFile = 'BodyCalc.ico'
mainWindow.iconbitmap(default=os.path.join(application_path, iconFile))


def get_bmi(weight, height):
    global bmi
    try:
        if not (weight and height):
            bmi = 'Error!'
        else:
            bmi = math.floor(int(weight) / (float(height) * float(height)))
    except ValueError:
        bmi = 'Error!'


def get_breast_multiplier(bust, cup):
    global breast_multiplier
    try:
        bust = int(bust)
        bust_scale = 'Below Average' if bust < 34 else 'Above Average'
    except ValueError:
        bust_scale = 'Error!'

    cup = cup.upper()
    if cup is '' and bust_scale is 'Error!':
        breast_multiplier = 99
    elif cup in ['AA', 'A'] and bust_scale is 'Below Average':
        breast_multiplier = 1
    elif cup in ['AA', 'A'] and bust_scale is 'Above Average':
        breast_multiplier = 2
    elif cup in ['B', 'C'] and bust_scale is 'Below Average':
        breast_multiplier = 2
    elif cup in ['D'] and bust_scale is 'Below Average':
        breast_multiplier = 3
    elif cup in ['B', 'C', 'D'] and bust_scale is 'Above Average':
        breast_multiplier = 3
    elif cup in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale is 'Below Average':
        breast_multiplier = 3
    elif cup in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale is 'Above Average':
        breast_multiplier = 4
    elif cup in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale is 'Below Average':
        breast_multiplier = 4
    elif cup in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale is 'Above Average':
        breast_multiplier = 5
    elif cup in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale is 'Below Average':
        breast_multiplier = 5
    elif cup in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale is 'Above Average':
        breast_multiplier = 6
    else:
        breast_multiplier = 0

    # Debugging purposes only!
    print(bust_scale, breast_multiplier)

    return breast_multiplier


def get_breast_desc(multiplier):
    global breast_desc
    if multiplier == 1:
        breast_desc = 'Tiny'
    elif multiplier == 2:
        breast_desc = 'Small'
    elif multiplier == 3:
        breast_desc = 'Medium'
    elif multiplier == 4:
        breast_desc = 'Large'
    elif multiplier == 5:
        breast_desc = 'Huge'
    elif multiplier == 6:
        breast_desc = 'Massive'
    elif multiplier == 99 or multiplier == 0:
        breast_desc = 'Error!'


def get_butt_desc(hip):
    global butt_desc
    try:
        hip = int(hip)
        if hip <= 32:
            butt_desc = 'Small'
        elif hip in range(33, 40):
            butt_desc = 'Medium'
        elif hip in range(40, 44):
            butt_desc = 'Large'
        elif hip in range(44, 48):
            butt_desc = 'Huge'
        elif hip >= 48:
            butt_desc = 'Massive'
    except ValueError:
        butt_desc = 'Error!'


def get_body_shape(bust, waist, hip):
    global body_shape
    try:
        bust = int(bust)
        waist = int(waist)
        hip = int(hip)

        # Waist is at least 25 percent smaller than Hip AND Bust measurement.
        if float(waist) * float(1.25) <= bust & hip:
            body_shape = 'Hourglass'

        # Hip measurement is more than 5 percent bigger than Bust measurement.
        elif float(hip) * float(1.05) > bust:
            body_shape = 'Pear'

        # Hip measurement is more than 5 percent smaller than Bust measurement.
        elif float(hip) * float(1.05) < bust:
            body_shape = 'Apple'

        # Bust, Waist and Hip measurements are within close range.
        high = max(bust, waist, hip)
        low = min(bust, waist, hip)
        difference = high - low

        # Debugging purposes only!
        print(high, low, difference)

        if difference <= 5:
            body_shape = 'Banana'
    except ValueError:
        body_shape = 'Error!'


def get_body_type(index, shape):
    global body_type
    type_descriptor = ''
    try:
        index = int(index)
        if index in range(1, 18):
            type_descriptor = 'A'
        elif index in range(18, 23):
            type_descriptor = 'B'
        elif index in range(23, 29):
            type_descriptor = 'C'
        elif index in range(29, 55):
            type_descriptor = 'D'
        elif index >= 55:
            type_descriptor = 'E'

        # Debugging purposes only!
        print(index, type_descriptor)

        if shape == 'Error!':
            body_type = 'Error!'
        elif type_descriptor == 'A':
            body_type = 'Skinny'
        elif type_descriptor == 'B':
            body_type = 'Petite'
        elif type_descriptor == 'C' and shape != 'Hourglass':
            body_type = 'Average'
        elif type_descriptor == 'C' and shape == 'Hourglass':
            body_type = 'Curvy'
        elif type_descriptor == 'D' and shape == 'Banana':
            body_type = 'BBW'
        elif type_descriptor == 'D' and shape == 'Hourglass':
            body_type = 'BBW - Curvy'
        elif type_descriptor == 'D' and shape == 'Pear':
            body_type = 'BBW - Bottom Heavy'
        elif type_descriptor == 'D' and shape == 'Apple':
            body_type = 'BBW - Top Heavy'
        elif type_descriptor == 'E' and shape == 'Banana' or shape == 'Hourglass':
            body_type = 'SSBBW'
        elif type_descriptor == 'E' and shape == 'Apple':
            body_type = 'SSBBW - Top Heavy'
        elif type_descriptor == 'E' and shape == 'Pear':
            body_type = 'SSBBW - Bottom Heavy'
    except ValueError:
        body_type = 'Error!'


def calculate(*args):
    global bmi
    global breast_desc
    global butt_desc
    global body_shape
    global body_type

    outputs = [bmiTxt, breastTxt, buttTxt, shapeTxt, typeTxt]

    list(map(lambda x: x.configure(state='normal'), outputs))
    list(map(lambda y: y.delete(1.0, END), outputs))

    get_bmi(weightIn.get(), heightIn.get())
    get_breast_multiplier(bustIn.get(), cupIn.get())
    get_breast_desc(breast_multiplier)
    get_butt_desc(hipIn.get())
    get_body_shape(bustIn.get(), waistIn.get(), hipIn.get())
    get_body_type(bmi, body_shape)

    bmiTxt.insert(END, bmi)
    breastTxt.insert(END, breast_desc)
    buttTxt.insert(END, butt_desc)
    shapeTxt.insert(END, body_shape)
    typeTxt.insert(END, body_type)

    list(map(lambda z: z.configure(state='disabled'), outputs))


def cleartxt(*args):
    inputs = [heightIn, weightIn, bustIn, cupIn, waistIn, hipIn]

    list(map(lambda x: x.delete(0, 'end'), inputs))
    heightIn.focus()


frameStyle = ttk.Style()
frameStyle.configure('TFrame', background='#444', foreground='white')
buttonStyle = ttk.Style()
buttonStyle.configure('TButton', background='gray', font=('Arial', '8', 'bold'))
labelStyle = ttk.Style()
labelStyle.configure('TLabel', background='#444', foreground='white', font=('Arial', '9'))
textFont = Font(family='Arial', size=9)

frameInput = ttk.Frame(mainWindow)
ttk.Label(frameInput, text='Height (M)').grid(row=0, column=0, pady=10)
ttk.Label(frameInput, text='Weight (KG)').grid(row=1, column=0, pady=10)
ttk.Label(frameInput, text='Bust / Cup').grid(row=2, column=0, pady=10)
ttk.Label(frameInput, text='Waist').grid(row=3, column=0, pady=10)
ttk.Label(frameInput, text='Hip').grid(row=4, column=0, pady=10)
heightIn = ttk.Entry(frameInput, width=4)
heightIn.grid(row=0, column=1, pady=8)
weightIn = ttk.Entry(frameInput, width=4)
weightIn.grid(row=1, column=1, pady=8)
bustIn = ttk.Entry(frameInput, width=4)
bustIn.grid(row=2, column=1, pady=8)
cupIn = ttk.Entry(frameInput, width=4)
cupIn.grid(row=2, column=2, padx=5, pady=8)
waistIn = ttk.Entry(frameInput, width=4)
waistIn.grid(row=3, column=1, pady=8)
hipIn = ttk.Entry(frameInput, width=4)
hipIn.grid(row=4, column=1, pady=8)


frameOutput = ttk.Frame(mainWindow)
ttk.Label(frameOutput, text='BMI').grid(row=0, column=0, pady=10)
ttk.Label(frameOutput, text='Breasts').grid(row=1, column=0, pady=10)
ttk.Label(frameOutput, text='Butt').grid(row=2, column=0, pady=10)
ttk.Label(frameOutput, text='Body Shape').grid(row=3, column=0, pady=10)
ttk.Label(frameOutput, text='Body Type').grid(row=4, column=0, pady=10)
bmiTxt = Text(frameOutput, state='disabled', width=10, height=1, bg='#444', fg='#fff', font=textFont, pady=5)
bmiTxt.grid(row=0, column=1, pady=5, sticky=W)
breastTxt = Text(frameOutput, state='disabled', width=10, height=1, bg='#444', fg='#fff', font=textFont, pady=5)
breastTxt.grid(row=1, column=1, pady=5, sticky=W)
buttTxt = Text(frameOutput, state='disabled', width=10, height=1, bg='#444', fg='#fff', font=textFont, pady=5)
buttTxt.grid(row=2, column=1, pady=5, sticky=W)
shapeTxt = Text(frameOutput, state='disabled', width=10, height=1, bg='#444', fg='#fff', font=textFont, pady=5)
shapeTxt.grid(row=3, column=1, pady=5, sticky=W)
typeTxt = Text(frameOutput, state='disabled', width=20, height=1, bg='#444', fg='#fff', font=textFont, pady=5)
typeTxt.grid(row=4, column=1, pady=5, sticky=W)

frameButtons = Frame(mainWindow)
frameButtons.configure(bg='#333')
ttk.Button(frameButtons, text='Calculate', width=10, command=calculate).grid(row=0, column=0, ipadx=1, padx=4)
ttk.Button(frameButtons, text='Clear', width=7, command=cleartxt).grid(row=0, column=1, ipadx=1, padx=4)

frameInput.grid(row=0, column=0, padx=10, pady=10)
frameOutput.grid(row=0, column=1, pady=10, ipadx=3)
frameButtons.grid(row=1, column=0, pady=5)

mainWindow.bind('<Return>', calculate)
mainWindow.bind('<\>', cleartxt)
mainWindow.mainloop()
