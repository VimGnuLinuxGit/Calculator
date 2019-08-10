#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Model software calculator
#==========================
# License: GNU GPL(v2.0)
# Software version 1.0
#==========================



class Model(object):

    # Functions ----------------------------------------------------------------------------------------#
    def press(self, char):
        self.entry.configure(stat='normal')
        self.entry.configure(foreground='green')
        self.entry.insert('end', char)

    def clearEntry(self):
        self.entry.configure(stat='normal')
        self.entry.configure(foreground='green')
        self.entry.delete('0', 'end')

    def delEndChar(self):       
        self.entry.configure(stat='normal')
        text = self.entry.get()[:-1]
        self.entry.delete('0', 'end')
        self.entry.insert('0', text)
    
    def equal(self):
        try:
            get = self.entry.get()
            if get == '':   # If entry as empty
                return
            for item in get:
                if item == '÷':
                    get = get.replace('÷', '/')
                elif item == 'x':
                    get = get.replace('x', '*')
                elif item == '%':
                    get = get.replace('%', '/100')
                elif item == '²':
                    get = get.replace('²', '**2')
                elif item in (',', ';', '^', '&', '|', '=', '!', '>', '<'):
                    get = 'Error'
            get = eval(get)
            self.entry.configure(stat='normal')
            self.entry.delete('0', 'end')
            self.entry.insert('0', get)
        except:
            self.entry.delete('0', 'end')
            self.entry.configure(foreground='red')
            self.entry.insert('0', 'Error')
            self.entry.configure(stat='readonly')



if __name__ == "__main__":
    pass
