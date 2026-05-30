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

