#!/usr/bin/python
import sys
from ..Lib import Msg

class Gui(object):
   def __init__(self, rxQue, txQue):
      self.rxQue = rxQue
      self.txQue = txQue
      self.processCmd = {
         "TestMsg" : self.testMsg,
         "ExitTest": self.exitProcess,}

   def exitProcess(self, msg):
      print "Exiting GUI!"
      self.done = True

   def testMsg(self,msg):
      print "GUI Received a test message:"
      print msg

   def runProcess(self):
      self.done = False
      while (not self.done):
         msg = self.rxQue.get()
         if msg.getMsgType() in self.processCmd.keys():
            self.processCmd[msg.getMsgType()](msg)
         else:
            print "Don't know how to handle msg:"
            print msg
            print "Keys: ", self.processCmd.keys()
      sys.stdout.flush()

def GuiInit(guiRx, guiTx):
   print "Starting GUI!"
   fil = open("dump","w")
   fil.write("Starting GUI")
   gui = Gui(guiRx, guiTx)
   gui.runProcess()

