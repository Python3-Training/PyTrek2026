# MISSION: PyTrek - The NEXT Generation.
# STATUS: Testing
# VERSION: 0.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek2026
# DATE: 2026-05-30 09:30:04
# FILE: console.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
import sys
if '..' not in sys.path:
    sys.path.append('..')
    
from PyTrek.abs_display import AbsDisplay
from PyTrek.points import *

class Con(AbsDisplay):
    '''
    The best place to start is by encapsulating the default
    display. Will add screen metadata for it all, later.
    '''
    def __init__(self):
        super().__init__(AbsDisplay.ST_CONSOLE)

    def display(self, message = ''):
        print(message)

    def read(self, prompt=''):
        return input(prompt)

    def read_double(self, prompt):
        text = input(prompt)
        try:
            value = float(text)
            return value
        except:
            pass
        return False

    def read_sector(self, prompt= "Helm: sector 1-64, speed 1.0-9.0?"):
        text = input(prompt + ': ')
        return WarpDest.parse(text)

    def read_xypos(self, prompt= "Helm: a-h, 1-8?"):
        text = input(prompt + ': ')
        return SubDest.parse(text)


if __name__ == '__main__':
    con = Con()
    con.display("Testing!")
    con.show_banner(["Testing, too!"])
    con.show_banner(["Testing", " .......... too!"])
