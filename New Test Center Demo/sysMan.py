#!/usr/bin/python

from Queue import Empty
from multiprocessing import Process, Queue
from ..Lib import Msg
from ..Gui import GuiInit
from ..TestMan import TestManInit
import time
import datetime

class SysMan(object):
   def __init__(self, testDir):
      self.testDir = testDir
      self.guiTxQ = Queue() 
      self.guiRxQ = Queue()
      self.testManTxQ = Queue()
      self.testManRxQ = Queue()
      self.gui = Process(target=GuiInit, args=(self.guiTxQ, self.guiRxQ))
      self.gui.start()
      self.testMan = Process(target=TestManInit, args=(self.testManTxQ, self.testManRxQ))
      self.testMan.start()

   def sendTestStationDetect(self):
      msg = Msg("TestStationDetect")
      msg.addItem("id", 1)
      msg.addItem("ip", "192.168.6.145")
      msg.addItem("state", "Present")
      msg.addItem("name", "Donald Duck")
      msg.addItem("mSwRev", "1.0.1")
      msg.addItem("mHwRev", "1.0P1")
      msg.addItem("pSwRev", "0.22S")
      msg.addItem("pHwRev", "0.33G")
      self.guiTxQ.put(msg)
      

   def sendCarrierBoardDetect(self):
      msg = Msg("CarrierBoardDetect")
      msg.addItem("id", 1)
      msg.addItem("carrierName", "Goofy")
      msg.addItem("hwRev", "1.1.1")
      msg.addItem("swRev", "N/A")
      msg.addItem("supportMdls", ["855", "855-IC", "842-DA"])
      msg.addItem("uboot", ["Revison A1","Revision A2", "Revision A3"])
      msg.addItem("kernel", ["Kernel A1","Kernel A2", "Kernel A3"])
      msg.addItem("application", ["App A1","App A2", "App A3"])
      msg.addItem("currModel", "855-IC")
      msg.addItem("currUboot", "Revision A2")
      msg.addItem("currApp", "App A3")
      msg.addItem("currKernel", "Kernel A1")
      self.guiTxQ.put(msg)

   def runProcess(self):
      # Just send a message to GUI and then test Manager and wait for 
      # a response from each.  Then send the ExitTest message.
      print "Sending message (SYS->GUI)"
      self.sendTestStationDetect()
      time.sleep(1)
      self.sendCarrierBoardDetect()

      while(True):
         try:
            msg = guiRxQ.get(timeout=0)

         except Empty:
            pass
         else:
            if msg.getMsgType() == "GetTcNames?":
               msg = Msg("GetTcNamesResp")
               msg.addItem("id", 1)
               msg.addItem("testCases", [["atod",0,True],["swamp",1,False],["test3",2,True]])
               print msg
               guiTxQ.put(msg)
         currTime = datetime.datetime.now() - start
         if currTime > datetime.timedelta(seconds=10):
            break
      mInput = raw_input("\nHit return to exit the process!\n")


      msg = Msg("ExitTest")
      msg.addItem("id", 1)
      self.guiTxQ.put(msg)
      self.testManTxQ.put(msg)
      self.gui.join()
      self.testMan.join()
      
def SysManInit(testDir):
   me = SysMan(testDir)
   print testDir
   me.runProcess()
