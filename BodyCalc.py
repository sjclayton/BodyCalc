from tkinter import *
import math
import os

mainWindow = Tk()

mainWindow.title('BodyCalc')
mainWindow.configure(background='#222')
mainWindow.minsize(460, 270)
mainWindow.maxsize(460, 270)

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


def get_breast_desc(bust, cup):
    global breast_desc
    try:
        bust = int(bust)
        bust_scale = 'Below Average' if bust < 34 else 'Above Average'
    except ValueError:
            bust_scale = 'Error!'

    cupout = cup.upper()
    if cupout is '' and bust_scale is 'Error!':
        breast_multiplier = 99
    elif cupout in ['AA', 'A'] and bust_scale is 'Below Average':
        breast_multiplier = 1
    elif cupout in ['AA', 'A'] and bust_scale is 'Above Average':
        breast_multiplier = 2
    elif cupout in ['B', 'C'] and bust_scale is 'Below Average':
        breast_multiplier = 2
    elif cupout in ['D'] and bust_scale is 'Below Average':
        breast_multiplier = 3
    elif cupout in ['B', 'C', 'D'] and bust_scale is 'Above Average':
        breast_multiplier = 3
    elif cupout in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale is 'Below Average':
        breast_multiplier = 3
    elif cupout in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'FF', 'G'] and bust_scale is 'Above Average':
        breast_multiplier = 4
    elif cupout in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale is 'Below Average':
        breast_multiplier = 4
    elif cupout in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I'] and bust_scale is 'Above Average':
        breast_multiplier = 5
    elif cupout in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale is 'Below Average':
        breast_multiplier = 5
    elif cupout in ['HHH', 'II', 'III', 'J', 'JJ', 'K'] and bust_scale is 'Above Average':
        breast_multiplier = 6
    else:
        breast_multiplier = 0

    # Debugging purposes only!
    print(bust_scale, breast_multiplier)

    if breast_multiplier == 1:
        breast_desc = 'Tiny'
    elif breast_multiplier == 2:
        breast_desc = 'Small'
    elif breast_multiplier == 3:
        breast_desc = 'Medium'
    elif breast_multiplier == 4:
        breast_desc = 'Large'
    elif breast_multiplier == 5:
        breast_desc = 'Huge'
    elif breast_multiplier == 6:
        breast_desc = 'Massive'
    elif breast_multiplier == 99 or breast_multiplier == 0:
        breast_desc = 'Error!'


def get_butt_desc(hip):
    global butt_desc
    try:
        if hip is '':
            butt_desc = 'Error!'
        elif int(hip) <= 32:
            butt_desc = 'Small'
        elif int(hip) in range(33, 40):
            butt_desc = 'Medium'
        elif int(hip) in range(40, 44):
            butt_desc = 'Large'
        elif int(hip) in range(44, 48):
            butt_desc = 'Huge'
        elif int(hip) >= 48:
            butt_desc = 'Massive'
        else:
            butt_desc = ''
    except ValueError:
        butt_desc = 'Error!'


def get_body_shape(bust, waist, hip):
    global body_shape
    try:
        bust = int(bust)
        waist = int(waist)
        hip = int(hip)

        # Waist is at least 25 percent smaller than Hip AND Bust measurement.
        if float(waist) * float(1.25) <= int(bust) & int(hip):
            body_shape = 'Hourglass'

        # Hip measurement is more than 5 percent bigger than Bust measurement.
        elif float(hip) * float(1.05) > int(bust):
            body_shape = 'Pear'

        # Hip measurement is more than 5 percent smaller than Bust measurement.
        elif float(hip) * float(1.05) < int(bust):
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


def calculate(event):
    global bmi
    global breast_desc
    global butt_desc
    global body_shape
    global body_type

    outputs = [bmiTxt, breastTxt, buttTxt, shapeTxt, typeTxt]

    list(map(lambda x: x.configure(state='normal'), outputs))
    list(map(lambda y: y.delete(1.0, END), outputs))

    get_bmi(weightIn.get(), heightIn.get())
    get_breast_desc(bustIn.get(), cupIn.get())
    get_butt_desc(hipIn.get())
    get_body_shape(bustIn.get(), waistIn.get(), hipIn.get())
    get_body_type(bmi, body_shape)

    bmiTxt.insert(END, bmi)
    breastTxt.insert(END, breast_desc)
    buttTxt.insert(END, butt_desc)
    shapeTxt.insert(END, body_shape)
    typeTxt.insert(END, body_type)

    list(map(lambda z: z.configure(state='disabled'), outputs))


def cleartxt(event):
    inputs = [heightIn, weightIn, bustIn, cupIn, waistIn, hipIn]

    list(map(lambda x: x.delete(0, 'end'), inputs))
    heightIn.focus()


frameMain = Frame(mainWindow)
frameMain.configure(bg='#444')
frameOutput = Frame(mainWindow)
frameOutput.configure(bg='#444')

heightLbl = Label(frameMain, text='Height (M)', bg='#444', fg='#fff').grid(row=0, column=0, pady=10)
heightIn = Entry(frameMain, width=4)
heightIn.grid(row=0, column=1, pady=10)
weightLbl = Label(frameMain, text='Weight (KG)', bg='#444', fg='#fff').grid(row=1, column=0, pady=10)
weightIn = Entry(frameMain, width=4)
weightIn.grid(row=1, column=1, pady=10)
bustLbl = Label(frameMain, text='Bust / Cup', bg='#444', fg='#fff').grid(row=2, column=0, pady=10)
bustIn = Entry(frameMain, width=4)
bustIn.grid(row=2, column=1, pady=10)
cupIn = Entry(frameMain, width=4)
cupIn.grid(row=2, column=2, padx=5, pady=10)
waistLbl = Label(frameMain, text='Waist', bg='#444', fg='#fff').grid(row=3, column=0, pady=10)
waistIn = Entry(frameMain, width=4)
waistIn.grid(row=3, column=1, pady=10)
hipLbl = Label(frameMain, text='Hip', bg='#444', fg='#fff').grid(row=4, column=0, pady=10)
hipIn = Entry(frameMain, width=4)
hipIn.grid(row=4, column=1, pady=10)

bmiLbl = Label(frameOutput, text='BMI', bg='#444', fg='#fff', pady=5)
bmiLbl.grid(row=0, column=0, pady=10)
bmiTxt = Text(frameOutput, state='disabled', width=10, height=1, bg='#444', fg='#fff', pady=5)
bmiTxt.grid(row=0, column=1, pady=5, sticky=W)
breastLbl = Label(frameOutput, text='Breasts', bg='#444', fg='#fff', pady=5)
breastLbl.grid(row=1, column=0, pady=5)
breastTxt = Text(frameOutput, state='disabled', width=10, height=1, bg='#444', fg='#fff', pady=5)
breastTxt.grid(row=1, column=1, pady=5, sticky=W)
buttLbl = Label(frameOutput, text='Butt', bg='#444', fg='#fff', pady=5)
buttLbl.grid(row=2, column=0, pady=5)
buttTxt = Text(frameOutput, state='disabled', width=10, height=1, bg='#444', fg='#fff', pady=5)
buttTxt.grid(row=2, column=1, pady=5, sticky=W)
shapeLbl = Label(frameOutput, text='Body Shape', bg='#444', fg='#fff', pady=5)
shapeLbl.grid(row=3, column=0, pady=5)
shapeTxt = Text(frameOutput, state='disabled', width=10, height=1, bg='#444', fg='#fff', pady=5)
shapeTxt.grid(row=3, column=1, pady=5, sticky=W)
typeLbl = Label(frameOutput, text='Body Type', bg='#444', fg='#fff', pady=5)
typeLbl.grid(row=4, column=0, pady=5)
typeTxt = Text(frameOutput, state='disabled', width=20, height=1, bg='#444', fg='#fff', pady=5)
typeTxt.grid(row=4, column=1, pady=5, sticky=W)

calcBtn = Button(mainWindow, text='Calculate', width=10)
calcBtn.bind('<Button-1>', calculate)
calcBtn.place(x=26, y=230)
clearBtn = Button(mainWindow, text='Clear', width=10)
clearBtn.bind('<Button-1>', cleartxt)
clearBtn.place(x=110, y=230)

frameMain.pack(side=LEFT, anchor=N, ipadx=5, padx=25, pady=10, fill=X)
frameOutput.pack(side=LEFT, anchor=N, ipadx=5, pady=10, fill=X)

mainWindow.bind('<Return>', calculate)
mainWindow.bind('<\>', cleartxt)
mainWindow.mainloop()
