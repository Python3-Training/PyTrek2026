# MISSION: PyTrek - The NEXT Generation.
# STATUS: Testing
# VERSION: 0.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek2026
# DATE: 2026-05-30 09:29:44
# FILE: abs_ship.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
import abc
import random

import sys
if '..' not in sys.path:
    sys.path.append('..')

from PyTrek import glyphs as Glyphs
from PyTrek import quips as Quips
from PyTrek.sector import Sector as Sector

class AbsShip(abc.ABC):
    ''' The first step, into a much larger universe ... '''

    def __init__(self):
        self.shield_level = 0

    @abc.abstractmethod
    def get_glyph(self):
        pass

