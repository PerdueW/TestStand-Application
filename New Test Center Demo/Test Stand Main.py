#!/usr/bin/python

from Tkinter import *
import Tkinter as tk
from ttk import *
import tkFont
import ttk
import wx
from actions2 import buttonaction
import sys



#creates the frame to house the graphical user interface components
sizex = 1190
sizey = 700
posx  = 300
posy  = 0
   
class gui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("Test Center 0001.1")
        self.grid()    
        
        def data():
            n=15
            self.btn = [1 for x in xrange(0,n*5+1)]
            self.myText = []
            
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
            canvas.configure(scrollregion=canvas.bbox("all"),width=1162,height=500)
    
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
        
        nbcanvas = Canvas(commport1,  width=1162, height=600) #creates the canvas in the notebook
        
        blanklbl3 = tk.Label(nbcanvas, text=" ")
        blanklbl3.grid(row=0, column=0)
        
        mdllbl = tk.Label(nbcanvas, text="  Model: ", font=helv8, bg="#000033", foreground="#FFFFFF")
        mdllbl.config(width=15)
        mdllbl.grid(row=1, column=0)
        
        mdl = StringVar()
        model = ttk.Combobox(nbcanvas, textvariable=mdl)
        model.bind(model)
        model['values'] = ('842')
        model.config(width=15)
        model.grid(row=1, column=1)

        mdlverlbl = tk.Label(nbcanvas, text="  Version: ", font=helv8, bg="#000033", foreground="#FFFFFF")
        mdlverlbl.config(width=15)
        mdlverlbl.grid(row=1, column=2)

        mdlversion = StringVar()
        mdlversion = ttk.Combobox(nbcanvas, textvariable=mdlversion)
        mdlversion.bind(model)
        mdlversion['values'] = ('842CA', '842DR', '842CZ')
        mdlversion.config(width=15)
        mdlversion.grid(row=1, column=3)

        applbl = tk.Label(nbcanvas, text="  Application: ", font=helv8, bg="#000033", foreground="#FFFFFF")
        applbl.config(width=15)
        applbl.grid(row=2, column=4)

        ubootlbl = tk.Label(nbcanvas, text="  Uboot: ", font=helv8, bg="#000033", foreground="#FFFFFF")
        ubootlbl.config(width=15)
        ubootlbl.grid(row=2, column=0)

        ubootversion = StringVar()
        ubootversion = ttk.Combobox(nbcanvas, textvariable=ubootversion)
        ubootversion.bind(model)
        ubootversion['values'] = ('UBoot A', 'UBoot B', 'UBoot C')
        ubootversion.config(width=15)
        ubootversion.grid(row=2, column=1)

        kernallbl = tk.Label(nbcanvas, text="  Kernal: ", font=helv8, bg="#000033", foreground="#FFFFFF")
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

        blanklbl3 = tk.Label(nbcanvas, text=" ")
        blanklbl3.grid(row=3, column=0)
        
        myframe=Frame(nbcanvas, width=1162,height=600,borderwidth=1)
        myframe.grid(row=4,columnspan=7)
        canvas=Canvas(myframe)
        frame=Frame(canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set, width=1162, height=600)
        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=frame,anchor='nw')
        frame.bind("<Configure>",myFunction)
        data()
        
        nbcanvas.grid() #adds the canvas to the notebook frame        
        notebook.add(commport1, text="Comm Port 1") #adds the first tab to the frame
        notebook.pack(fill=BOTH, padx=2, pady=3) # adds notebook to the frame
        
    def setButtonText(self, btnid, text):
        self.myText[btnid].set(text)

        
root = Tk() #creates the window that will contain all the components of the gui portion of the application
app = gui(master=root)

root.wm_geometry("%dx%d+%d+%d" % (sizex,sizey,posx,posy)) # sets the size of the main window
root.resizable(width=FALSE, height=FALSE) # disables the ability to resize the window
root.configure(background='DODGERBLUE')
app.mainloop()
