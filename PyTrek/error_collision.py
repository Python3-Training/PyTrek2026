# MISSION: PyTrek - The NEXT Generation.
# STATUS: Testing
# VERSION: 0.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek2026
# DATE: 2026-05-30 09:21:29
# FILE: error_collision.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
class ErrorEnterpriseCollision(Exception):
    '''
    ... because some problems simply have to wait ... =)
    '''
    def __init__(self, glyph):
        super().__init__()
        self.glyph = glyph


