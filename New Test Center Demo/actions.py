#!/usr/bin/python

from Tkinter import *
import Tkinter as tk
from ttk import *
import tkFont
import ttk
import wx
import sys
from tkMessageBox import *

#from TestCenter0001 import *

def buttonaction(btnid,btnVar):
    if btnid == 1:
        btnVar.set("Test 1 changed my text")
    if btnid == 2:
        btnVar.set("Test 2 changed by text")


def printHello(btnid):
    if btnid == 1:
        text="Changed by Button Press"
    else:
        print("Button " +str(btnid) + " was Pressed!")
        


def answer():
    showerror("Answer", "Sorry, no answer available")

def callback():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')


