#!/usr/bin/python

import os
from testBed import SysManInit

if __name__ == "__main__":
    SysManInit(os.path.dirname(os.path.realpath(__file__))+'/TestFiles')
