#!/usr/bin/python

from Tkinter import *
import Tkinter as tk
#from TestCenter0001 import *

#def buttonaction(btn0,test,otherBtn=None):
#           """toggle button text between Hi and Goodbye"""
#           if btn0["text"] == "Hi"+test:
###                # switch to Goodbye
#                btn0["text"] = "Goodbye"+test
#           else:
#               # reset to Hi
#                btn0["text"] = "Hi"+test
#           if otherBtn is not None:
#               otherBtn.set("My Text Changed")
"""
def buttonaction(src,btnVar):
    if src == "test 1":
        btnVar.set("Test 1 changed my text")
    if src == "test 2":
        btnVar.set("Test 2 changed by text")
"""

def buttonaction(src,btnid,GUI):
    if src == "test 1":
        GUI.setButtonText(btnid, "Test 1 changed my text")
    GUI.setButtonText(12,"I'm Batman!")
        
 

