from socket import SHUT_WR
import traceback
from pyp3d import *

class 电线(Component):
    def __init__(self):
        Component.__init__(self)
        self['a']=Attr(False,obvious=True)
        self['电线']=Attr(None,show=True)
        self.replace()
    def replace(self):
       
if __name__=="__main__":
    final=电线()
    place(final)