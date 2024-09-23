#!/usr/bin/python

from Tkinter import *
import Tkinter as tk
from ttk import *
import tkFont
import ttk
import wx

#creates the frame to house the graphical user interface components
class gui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("Test Center 0001")
        self.grid()

        helv8 = tkFont.Font(family='Helvetica', size=8, weight='bold')
        helv9 = tkFont.Font(family='Helvetica', size=9, weight='bold')
        helv10 = tkFont.Font(family='Helvetica', size=10, weight='bold')
        helv11 = tkFont.Font(family='Helvetica', size=11, weight='bold')
        helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold')
        helv14 = tkFont.Font(family='Helvetica', size=14, weight='bold')        
        
        #creates the notebook to give the tab features of the application
        notebook = Notebook(root)
        s = Style()
        s.configure('commport1.TFrame', background='#000033')

        #creates the first tab of the gui
        commport1 = Frame(notebook, style='commport1.TFrame')

        nbcanvas = Canvas(commport1,  width=800, height=800) #creates the canvas in the notebook

        mdllbl = tk.Label(nbcanvas, text="  Model: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        mdllbl.config(width=20)
        mdllbl.grid(row=0, column=0)
        
        mdl = StringVar()
        model = ttk.Combobox(nbcanvas, textvariable=mdl)
        model.bind(model)
        model['values'] = ('842')
        model.config(width=20)
        model.grid(row=0, column=1)

        mdlverlbl = tk.Label(nbcanvas, text="  Version: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        mdlverlbl.config(width=20)
        mdlverlbl.grid(row=0, column=2)

        mdlversion = StringVar()
        mdlversion = ttk.Combobox(nbcanvas, textvariable=mdlversion)
        mdlversion.bind(model)
        mdlversion['values'] = ('842CA', '842DR', '842CZ')
        mdlversion.config(width=20)
        mdlversion.grid(row=0, column=3)

        blanklbl1 = tk.Label(nbcanvas, text=" ")
        blanklbl1.config(width=20)
        blanklbl1.grid(row=0, column=4)

        blanklbl2 = tk.Label(nbcanvas, text=" ")
        blanklbl2.config(width=20)
        blanklbl2.grid(row=0, column=5)

        ubootlbl = Label(nbcanvas, text="  Uboot: ")
        ubootlbl.config(width=20)
        ubootlbl.grid(row=1, column=0)

        ubootlbl = tk.Label(nbcanvas, text="  Uboot: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        ubootlbl.config(width=20)
        ubootlbl.grid(row=1, column=0)

        ubootversion = StringVar()
        ubootversion = ttk.Combobox(nbcanvas, textvariable=ubootversion)
        ubootversion.bind(model)
        ubootversion['values'] = ('UBoot A', 'UBoot B', 'UBoot C')
        ubootversion.config(width=20)
        ubootversion.grid(row=1, column=1)

        kernallbl = tk.Label(nbcanvas, text="  Kernal: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        kernallbl.config(width=20)
        kernallbl.grid(row=1, column=2)

        kernalversion = StringVar()
        kernalversion = ttk.Combobox(nbcanvas, textvariable=kernalversion)
        kernalversion.bind(model)
        kernalversion['values'] = ('Kernal A', 'Kernal B', 'Kernal C')
        kernalversion.config(width=20)
        kernalversion.grid(row=1, column=3)

        applbl = tk.Label(nbcanvas, text="  Application: ", font=helv9, bg="#000033", foreground="#FFFFFF")
        applbl.config(width=20)
        applbl.grid(row=1, column=4)

        appversion = StringVar()
        appversion = ttk.Combobox(nbcanvas, textvariable=appversion)
        appversion.bind(model)
        appversion['values'] = ('App A', 'App B', 'App C')
        appversion.config(width=20)
        appversion.grid(row=1, column=5)


        nbcanvas.grid() #adds the canvas to the notebook frame        
        notebook.add(commport1, text="Comm Port 1") #adds the first tab to the frame
        notebook.pack(fill=BOTH, padx=2, pady=3) # adds notebook to the frame
        
root = Tk() #creates the window that will contain all the components of the gui portion of the application
app = gui(master=root)
root.geometry('879x800+500+100') # sets the size of the main window
root.resizable(width=FALSE, height=FALSE) # disables the ability to resize the window
root.configure(background='DODGERBLUE')
app.mainloop()
