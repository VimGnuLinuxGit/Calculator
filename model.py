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
        if self.entry.get()[:] == 'Error':    # Do nothing
            return
        self.entry.configure(stat='normal')
        self.entry.configure(foreground='green')
        self.entry.insert('end', char)

    def clearEntry(self):
        self.entry.configure(stat='normal')
        self.entry.configure(foreground='green')
        self.entry.delete('0', 'end')

    def delEndChar(self):       
        if self.entry.get()[:] == 'Error':    # Do nothing
            return
        self.entry.configure(stat='normal')
        text = self.entry.get()[:-1]
        self.entry.delete('0', 'end')
        self.entry.insert('0', text)
    
    def power(self):
        resultEqual = self.equal()
        if resultEqual == None:    # Do nothing
            return
        self.entry.configure(stat='normal')
        self.entry.delete('0', 'end')
        self.entry.insert('0', pow(resultEqual, 2))
    
    def equal(self):
        getEntry = self.entry.get()
        try:
            if len(getEntry) == 0:    # If entry as empty: do nothing 
                return 
            for item in getEntry:
                if item in (',', ';', '^', '&', '|', '=', '!', '>', '<'):
                    getEntry = 'Error input character'    # If characters input the are these: eval Error
                    break
                elif item == '÷':
                    getEntry = getEntry.replace('÷', '/')
                elif item == 'x':
                    getEntry = getEntry.replace('x', '*')
                elif item == '%':
                    getEntry = getEntry.replace('%', '/100')
            resultEqual = eval(getEntry)
            self.entry.configure(stat='normal')
            self.entry.delete('0', 'end')
            self.entry.insert('0', resultEqual)
            return resultEqual
        except:
            self.entry.delete('0', 'end')
            self.entry.configure(foreground='red')
            self.entry.insert('0', 'Error')
            self.entry.configure(stat='readonly')
            return


if __name__ == "__main__":
    pass
