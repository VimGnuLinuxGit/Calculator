#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# Main software calculator
#=========================
# License: GNU GPL(v2.0) 
# Software version 1.0   
#=========================

from model import *
from view import *



if __name__ == "__main__":
    root = Tk()
    app = View(root)
    root.mainloop()
