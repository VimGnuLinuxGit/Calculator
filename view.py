#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# View software calculator
#=========================
# License: GNU GPL(v2.0) 
# Software version 1.0   
#=========================

from tkinter import *
from model import Model



class View(Model):
    
    def __init__(self, master):
        self.master = master
        self.master.title('Calculator')
        self.master.resizable(width=False, height=False)
        self.master.configure(background='tan')

        self.font = ('Aria', 12, 'bold')
        self.entry = Entry(self.master, background='wheat', foreground='green', font=self.font)


        # Buttons --------------------------------------------------------------------------------------#
        self.button0 = Button(self.master, text='0', background='tan', font=self.font, 
                command=lambda: self.press('0'))
        self.button1 = Button(self.master, text='1', background='tan', font=self.font, 
                command=lambda: self.press('1'))
        self.button2 = Button(self.master, text='2', background='tan', font=self.font, 
                command=lambda: self.press('2'))
        self.button3 = Button(self.master, text='3', background='tan', font=self.font,
                command=lambda: self.press('3'))
        self.button4 = Button(self.master, text='4', background='tan', font=self.font,
                command=lambda: self.press('4'))
        self.button5 = Button(self.master, text='5', background='tan', font=self.font,
                command=lambda: self.press('5'))
        self.button6 = Button(self.master, text='6', background='tan', font=self.font,
                command=lambda: self.press('6'))
        self.button7 = Button(self.master, text='7', background='tan', font=self.font,
                command=lambda: self.press('7'))
        self.button8 = Button(self.master, text='8', background='tan', font=self.font, 
                command=lambda: self.press('8'))
        self.button9 = Button(self.master, text='9', background='tan', font=self.font,
                command=lambda: self.press('9'))
        self.buttonPoint = Button(self.master, text='.', background='tan', font=self.font,
                command=lambda: self.press('.'))
        self.buttonPercent = Button(self.master, text='%', background='tan', font=self.font, 
                command=lambda: self.press('%'))
        self.buttonSum = Button(self.master, text='+', background='tan', font=self.font,
                command=lambda: self.press('+'))
        self.buttonMinus = Button(self.master, text='-', background='tan', font=self.font, 
                command=lambda: self.press('-'))
        self.buttonMultiply = Button(self.master, text='x', background='tan', font=self.font,
                command=lambda: self.press('x'))
        self.buttonDivide = Button(self.master, text='÷', background='tan', font=self.font,
                command=lambda: self.press('÷'))
        self.buttonAC = Button(self.master, text='AC', background='tan', font=self.font, activeforeground='red',
                command=self.clearEntry)
        self.buttonClearCh = Button(self.master, text='⤟', background='tan', font=self.font,
                command=self.delEndChar)
        self.buttonPower = Button(self.master, text='x²', background='tan', font=self.font,
                command=self.power)
        self.buttonEqual = Button(self.master, text='=', background='tan', font=self.font, 
                activeforeground='green', command=self.equal)


        # Grid -----------------------------------------------------------------------------------------#
        self.entry.grid(row=0, column=0, columnspan=5, sticky='EW', padx=5, pady=5)
        self.button7.grid(row=1, column=0,  padx=5, pady=3, sticky='EW')
        self.button8.grid(row=1, column=1, padx=5, sticky='EW')
        self.button9.grid(row=1, column=2, padx=5, sticky='EW')
        self.buttonDivide.grid(row=1, column=3, padx=5, sticky='EW')
        self.buttonClearCh.grid(row=2, column=4, padx=5, sticky='EW')
        self.buttonAC.grid(row=1, column=4, padx=5, sticky='EW')
        self.button4.grid(row=2, column=0, padx=5, pady=2, sticky='EW')
        self.button5.grid(row=2, column=1, padx=5, sticky='EW')
        self.button6.grid(row=2, column=2, padx=5, sticky='EW')
        self.buttonMultiply.grid(row=2, column=3, padx=5, sticky='EW')
        self.button1.grid(row=3, column=0, padx=5, pady=2, sticky='EW')
        self.button2.grid(row=3, column=1, padx=5, sticky='EW')
        self.button3.grid(row=3, column=2, padx=5, sticky='EW')
        self.buttonMinus.grid(row=3, column=3, padx=5, sticky='EW')
        self.buttonPower.grid(row=3, column=4, padx=5, sticky='EW')
        self.button0.grid(row=4, column=0, padx=5, pady=3, sticky='EW')
        self.buttonPoint.grid(row=4, column=1, padx=5, sticky='EW')
        self.buttonPercent.grid(row=4, column=2, padx=5, sticky='EW')
        self.buttonSum.grid(row=4, column=3, padx=5, sticky='EW')
        self.buttonEqual.grid(row=4, column=4, columnspan=5, sticky='EW', padx=5)



if __name__ == "__main__":
    root = Tk()
    app = View(root)
    root.mainloop()
