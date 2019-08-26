#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Model software calculator
#==========================
# License: GNU GPL(v2.0)
# Software version 1.0
#==========================



class Model(object):

    # Functions ----------------------------------------------------------------------------------------#
    def clearEntry(self):
        self.entry.configure(stat='normal')
        self.entry.configure(foreground='green')
        self.entry.delete('0', 'end')

    def delEndChar(self):
        text = self.entry.get()[:-1]
        self.entry.delete('0', 'end')
        self.entry.insert('0', text)

    def press(self, char):
        if dict(self.entry)['state'] == 'normal':
            self.entry.insert('end', char)

    def power(self):
        resultPower = self.tryExcept()
        if resultPower != None:
            self.entry.delete('0', 'end')
            self.entry.insert('0', pow(resultPower, 2))

    def equal(self):
        resultEqual = self.tryExcept()
        if resultEqual != None:
            self.entry.delete('0', 'end')
            self.entry.insert('0', resultEqual)

    def tryExcept(self):
        getEntry = self.entry.get()
        if len(getEntry) == 0:    # If entry as empty: do nothing 
            return None 
        for item in getEntry:
            if item in (',', ';', '^', '&', '|', '=', '!', '>', '<'):
                getEntry = 'Error'    # If characters input the are these: eval Error and SyntaxError
                break
            elif item == '÷':
                getEntry = getEntry.replace('÷', '/')
            elif item == 'x':
                getEntry = getEntry.replace('x', '*')
            elif item == '%':
                getEntry = getEntry.replace('%', '/100')
        try:
            resultTryExcept = eval(getEntry)
            return resultTryExcept
        except (SyntaxError, NameError):    # If entry value is Error: NameError
            self.entry.delete('0', 'end')
            self.entry.configure(foreground='red')
            self.entry.insert('0', 'Error')
            self.entry.configure(stat='readonly')
            return None



if __name__ == "__main__":
    pass
