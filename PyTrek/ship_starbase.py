# MISSION: PyTrek - The NEXT Generation.
# STATUS: Testing
# VERSION: 0.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek2026
# DATE: 2026-05-30 09:32:12
# FILE: ship_starbase.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
import sys
if '..' not in sys.path:
    sys.path.append('..')

import PyTrek.glyphs as Glyphs
from PyTrek.abs_ship import AbsShip as AbsShip

class ShipStarbase(AbsShip):

    def __init__(self):
        super().__init__()

    def get_glyph(self):
        return Glyphs.STARBASE

    @staticmethod
    def dock_enterprise(ship):
        ship.energy = 3000
        ship.photon_torpedoes = 10
        ship.navigation_damage = 0
        ship.short_range_scan_damage = 0
        ship.long_range_scan_damage = 0
        ship.shield_control_damage = 0
        ship.computer_damage = 0
        ship.photon_damage = 0
        ship.phaser_damage = 0
        ship.shield_level = 0
        ship.docked = True

    @staticmethod
    def launch_enterprise(ship):
        ship.docked = False
