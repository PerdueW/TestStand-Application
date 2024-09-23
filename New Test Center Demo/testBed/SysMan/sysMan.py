#!/usr/bin/python

from multiprocessing import Process, Queue
from ..Lib import Msg
from ..Gui import GuiInit
from ..TestMan import TestManInit
import time

class SysMan(object):
   def __init__(self, testDir):
      self.testDir = testDir
      self.guiTxQ = Queue() 
      self.guiRxQ = Queue()
      self.testManTxQ = Queue()
      self.testManRxQ = Queue()
      self.gui = Process(target=GuiInit, args=(self.guiTxQ, self.guiRxQ))
      print "Starting gui!"
      self.gui.start()
      self.testMan = Process(target=TestManInit, args=(self.testManTxQ, self.testManRxQ))
      self.testMan.start()

   def runProcess(self):
      # Just send a message to GUI and then test Manager and wait for 
      # a response from each.  Then send the ExitTest message.
      print "Sending message (SYS->GUI)"
      msg = Msg("TestMsg")
      msg.addItem("id", "TestMessage1")
      self.guiTxQ.put(msg)
      self.testManTxQ.put(msg)


      time.sleep(5)
      mInput = raw_input("\nHit return to exit the process!\n")


      msg = Msg("ExitTest")
      msg.addItem("id", "TestStation1")
      self.guiTxQ.put(msg)
      self.testManTxQ.put(msg)
      time.sleep(1)
      self.gui.join()
      self.testMan.join()
      
def SysManInit(testDir):
   me = SysMan(testDir)
   print testDir
   me.runProcess()
