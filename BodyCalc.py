from tkinter import *
import math

mainWindow = Tk()

mainWindow.title('Body Stats Calculator')
mainWindow.iconbitmap('BodyCalc.ico')
mainWindow.configure(background='#222')
mainWindow.minsize(460, 270)
mainWindow.maxsize(460, 270)


def get_bmi(weightIn, heightIn):
    global bmi
    if weightIn is '' or heightIn is '':
        bmi = 0
    else:
        bmi = math.floor(int(weightIn) / (float(heightIn) * float(heightIn)))


def get_breast_desc(cupIn):
    global breast_desc
    if cupIn is '':
        breast_multiplier = 99
    elif cupIn in ['AA', 'A']:
        breast_multiplier = 1
    elif cupIn in ['B']:
        breast_multiplier = 2
    elif cupIn in ['C', 'D']:
        breast_multiplier = 3
    elif cupIn in ['DD', 'DDD', 'E', 'EE', 'EEE', 'F', 'G']:
        breast_multiplier = 4
    elif cupIn in ['FFF', 'GG', 'GGG', 'H', 'HH', 'I']:
        breast_multiplier = 5
    elif cupIn in ['HHH', 'II', 'III', 'JJ', 'K']:
        breast_multiplier = 6
    else:
        breast_multiplier = 0

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
    elif breast_multiplier == 99:
        breast_desc = 'Error!'
    else:
        breast_desc = ''


def get_butt_desc(hipIn):
    global butt_desc
    if hipIn is '':
        butt_desc = 'Error!'
    elif int(hipIn) <= 34:
        butt_desc = 'Small'
    elif int(hipIn) in range(35,39):
        butt_desc = 'Medium'
    elif int(hipIn) in range(39,44):
        butt_desc = 'Large'
    elif int(hipIn) >= 44:
        butt_desc = 'Huge'
    else:
        butt_desc = ''


def get_body_shape(bustIn, waistIn, hipIn):
    global body_shape
    try:
        inputBust = int(bustIn)
        inputWaist = int(waistIn)
        inputHip = int(hipIn)

        # Waist is at least 25 percent smaller than Hip AND Bust measurement.
        if float(inputWaist) * float(1.25) <= int(bustIn) & int(hipIn):
            body_shape = 'Hourglass'

        # Hip measurement is more than 5 percent bigger than Bust measurement.
        elif float(inputHip) * float(1.05) > int(bustIn):
            body_shape = 'Pear'

        # Hip measurement is more than 5 percent smaller than Bust measurement.
        elif float(inputHip) * float(1.05) < int(bustIn):
            body_shape = 'Apple'

        # Bust, Waist and Hip measurements are within close range.
        highVal = max(inputBust, inputWaist, inputHip)
        lowVal = min(inputBust, inputWaist, inputHip)
        difference = highVal - lowVal

        print(highVal, lowVal, difference)
        if int(difference) <= 5:
            body_shape = 'Banana'

    except ValueError:
            body_shape = 'Error!'


def get_body_type(bmi, shape):
    global body_type
    type_descriptor = ''
    if int(bmi) in range(1, 17):
        type_descriptor = 'A'
    elif int(bmi) in range(17,20):
        type_descriptor = 'B'
    elif int(bmi) in range(20,25):
        type_descriptor = 'C'
    elif int(bmi) in range(25,30):
        type_descriptor = 'D'
    elif int(bmi) > 30:
        type_descriptor = 'E'

    print(type_descriptor)

    if int(bmi) == 0:
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
    elif type_descriptor == 'E':
        body_type = 'SSBBW'
    else:
        body_type = ''


def calculate():
    global bmi
    global breast_desc
    global butt_desc
    global body_shape
    global body_type
    bmiTxt.delete(1.0, END)
    get_bmi(weightIn.get(), heightIn.get())
    bmiTxt.insert(END, bmi)
    breastTxt.delete(1.0, END)
    get_breast_desc(cupIn.get())
    breastTxt.insert(END, breast_desc)
    buttTxt.delete(1.0, END)
    get_butt_desc(hipIn.get())
    buttTxt.insert(END, butt_desc)
    shapeTxt.delete(1.0, END)
    get_body_shape(bustIn.get(), waistIn.get(), hipIn.get())
    shapeTxt.insert(END, body_shape)
    typeTxt.delete(1.0, END)
    get_body_type(bmi, body_shape)
    typeTxt.insert(END, body_type)


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
bmiTxt = Text(frameOutput, width=10, height=1, bg='#444', fg='#fff', pady=5)
bmiTxt.grid(row=0, column=1, pady=5, sticky=W)
breastLbl = Label(frameOutput, text='Breasts', bg='#444', fg='#fff', pady=5)
breastLbl.grid(row=1, column=0, pady=5)
breastTxt = Text(frameOutput, width=10, height=1, bg='#444', fg='#fff', pady=5)
breastTxt.grid(row=1, column=1, pady=5, sticky=W)
buttLbl = Label(frameOutput, text='Butt', bg='#444', fg='#fff', pady=5)
buttLbl.grid(row=2, column=0, pady=5)
buttTxt = Text(frameOutput, width=10, height=1, bg='#444', fg='#fff', pady=5)
buttTxt.grid(row=2, column=1, pady=5, sticky=W)
shapeLbl = Label(frameOutput, text='Body Shape', bg='#444', fg='#fff', pady=5)
shapeLbl.grid(row=3, column=0, pady=5)
shapeTxt = Text(frameOutput, width=10, height=1, bg='#444', fg='#fff', pady=5)
shapeTxt.grid(row=3, column=1, pady=5, sticky=W)
typeLbl = Label(frameOutput, text='Body Type', bg='#444', fg='#fff', pady=5)
typeLbl.grid(row=4, column=0, pady=5)
typeTxt = Text(frameOutput, width=20, height=1, bg='#444', fg='#fff', pady=5)
typeTxt.grid(row=4, column=1, pady=5, sticky=W)

calcBtn = Button(mainWindow, text='Calculate', width=10, command=calculate)
calcBtn.place(x=57, y=230)

frameMain.pack(side=LEFT, anchor=N, ipadx=5, padx=25, pady=10, fill=X)
frameOutput.pack(side=LEFT, anchor=N, ipadx=5, pady=10, fill=X)

mainWindow.mainloop()