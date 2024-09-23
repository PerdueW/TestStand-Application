#!/usr/bin/python

from Tkinter import *
import Tkinter as tk
from ttk import *
import tkFont
import ttk
import wx
from actions2 import buttonaction
import sys
from DataManipulator import *
import os
import thread
import time



#creates the frame to house the graphical user interface components
sizex = 1200
sizey = 660
posx  = 300
posy  = 0
   
class gui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("Test Center 0001.1")
        self.grid()
       
        btnid=0
        self.myText = []
        #myText.set("Button 0")
        n=15
        
        def data():
            #self.btn = [[1 for x in xrange(n)] for x in xrange(n)]
            self.btn = [1 for x in xrange(0,n*5+1)]
            btnid=0
            self.myText.append(StringVar()) 
            for y in range(n):          
                for x in range(5):
                    self.myText.append(StringVar())
                    self.myText[y*5+x].set("Button: "+ str(btnid))
                    self.btn[btnid] = tk.Button(frame, textvar=self.myText[btnid], command=lambda t=(btnid): buttonaction("test 1",t,self),  font=helv8, height='5', width='30', padx=7, pady=7, bg="#000000", foreground="GREEN")
                    self.btn[btnid].grid(column=x+1, row=y+1)
                    btnid+=1
                 
        def myFunction(event):
            canvas.configure(scrollregion=canvas.bbox("all"),width=1170,height=475)
    
        helv8 = tkFont.Font(family='Helvetica', size=8, weight='bold')
        helv9 = tkFont.Font(family='Helvetica', size=9, weight='bold')
        helv10 = tkFont.Font(family='Helvetica', size=10, weight='bold')
        helv11 = tkFont.Font(family='Helvetica', size=11, weight='bold')
        helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold')
        helv14 = tkFont.Font(family='Helvetica', size=14, weight='bold')        
        
        #creates the notebook to give the tab features of the application
        notebook = Notebook(root)
        s = Style()
        s.configure('commport1.TFrame', background="#0066CC")
        
        
        #creates the first tab of the gui
        commport1 = Frame(notebook, style='commport1.TFrame')
        
        nbcanvas = Canvas(commport1,  width=1200, height=655, bg="#0066CC") #creates the canvas in the notebook
        
        blanklbl1 = tk.Label(nbcanvas, text=" ", bg="#0066CC")
        blanklbl1.grid(row=0, column=0)
        
        mdllbl = tk.Label(nbcanvas, text="  Model: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        mdllbl.config(width=15)
        mdllbl.grid(row=1, column=0)
        
        mdl = StringVar()
        model = ttk.Combobox(nbcanvas, textvariable=mdl)
        model.bind(model)
        model['values'] = dataManipulator.model
        model.config(width=15)
        model.grid(row=1, column=1)

        mdlverlbl = tk.Label(nbcanvas, text="  Version: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        mdlverlbl.config(width=15)
        mdlverlbl.grid(row=1, column=2)

        mdlversion = StringVar()
        mdlversion = ttk.Combobox(nbcanvas, textvariable=mdlversion)
        mdlversion.bind(model)
        mdlversion['values'] = dataManipulator.version
        mdlversion.config(width=15)
        mdlversion.grid(row=1, column=3)

        exitbtn = tk.Button(nbcanvas, text ="Close", command = close_window, font=helv9, height='1', width='15', bg="#330000", foreground="#FFFFFF")
        exitbtn.grid(row=0, column=5)

        applbl = tk.Label(nbcanvas, text="  Application: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        applbl.config(width=15)
        applbl.grid(row=2, column=4)

        ubootlbl = tk.Label(nbcanvas, text="  Uboot: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        ubootlbl.config(width=15)
        ubootlbl.grid(row=2, column=0)

        ubootversion = StringVar()
        ubootversion = ttk.Combobox(nbcanvas, textvariable=ubootversion)
        ubootversion.bind(model)
        ubootversion['values'] = ('UBoot A', 'UBoot B', 'UBoot C')
        ubootversion.config(width=15)
        ubootversion.grid(row=2, column=1)

        kernallbl = tk.Label(nbcanvas, text="  Kernal: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        kernallbl.config(width=15)
        kernallbl.grid(row=2, column=2)

        kernalversion = StringVar()
        kernalversion = ttk.Combobox(nbcanvas, textvariable=kernalversion)
        kernalversion.bind(model)
        kernalversion['values'] = ('Kernal A', 'Kernal B', 'Kernal C')
        kernalversion.config(width=15)
        kernalversion.grid(row=2, column=3)

        appversion = StringVar()
        appversion = ttk.Combobox(nbcanvas, textvariable=appversion)
        appversion.bind(model)
        appversion['values'] = ('App A', 'App B', 'App C')
        appversion.config(width=15)
        appversion.grid(row=2, column=5)

        blanklbl2 = tk.Label(nbcanvas, text=" ", bg="#0066CC")
        blanklbl2.grid(row=3, column=0)
        
        myframe=Frame(nbcanvas, width=1162,height=600,borderwidth=1)
        myframe.grid(row=4,columnspan=7)
        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set)

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myFunction)
        data()

        startbtn = tk.Button(nbcanvas, text ="Start", command=processStart, font=helv9, height='2', width='15', bg="#006600", foreground="#FFFFFF")
        startbtn.grid(row=5, column=2)
        pausebtn = tk.Button(nbcanvas, text ="Pause", command=processPause, font=helv9, height='2', width='15', bg="#CCCC33", foreground="#000000")
        pausebtn.grid(row=5, column=3)
        pausebtn = tk.Button(nbcanvas, text ="Stop", command=processStop, font=helv9, height='2', width='15', bg="#CC0000", foreground="#FFFFFF")
        pausebtn.grid(row=5, column=4)
        exitbtn = tk.Button(nbcanvas, text ="Exit", command = processExit, font=helv9, height='2', width='15', bg="#330000", foreground="#FFFFFF")
        exitbtn.grid(row=5, column=5)
        
        
        nbcanvas.grid() #adds the canvas to the notebook frame        
        notebook.add(commport1, text="Comm Port 1") #adds the first tab to the frame
        notebook.pack(fill=BOTH, padx=2, pady=3) # adds notebook to the frame
        
    def setButtonText(self, btnid, text):
        self.myText[btnid].set(text)

def close_window (): 
    root.destroy()

        
root = Tk() #creates the window that will contain all the components of the gui portion of the application
app = gui(master=root)

root.wm_geometry("%dx%d+%d+%d" % (sizex,sizey,posx,posy)) # sets the size of the main window
root.resizable(width=FALSE, height=FALSE) # disables the ability to resize the window
root.configure(background='DODGERBLUE')
app.mainloop()
