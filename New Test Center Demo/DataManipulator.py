#!/usr/bin/python

from Tkinter import *
import Tkinter as tk
from ttk import *
import tkFont, ttk, wx, sys, os
from actions2 import buttonaction
import os
import thread
import time


class dataManipulator:
        #model = []
        #version = []
        data = []
        infile = open("842.txt", "r")
        for line in open("842.txt").readlines():
                model, version = line.split()
                model = str(model)
                version = str(version)
                data.append((model,version))
        
        print("Name of your file is: ", infile.name)
        print infile.read()
        print "Model:" + model, "Version(s):" + version
        print model
        print version
        print data
       
        infile.close()

def processStart():                             
                print("Test Started!")

def processPause():
                print("Test Paused!")
                
def processStop():
                print("Test Stopped!")

def processExit():
                print("Test Exited!")


                
            

    
    
