#!/usr/bin/python

from ..Lib import Msg

class TestMan(object):
   def __init__(self, rxQue, txQue):
      self.rxQue = rxQue
      self.txQue = txQue
      self.processCmd = {
         "TestMsg" : self.testMsg,
         "ExitTest": self.exitProcess,}

   def exitProcess(self, msg):
      print "Exiting TestMan!"
      self.done = True

   def testMsg(self,msg):
      print "TestMan Received a test message:"
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

def TestManInit(testManRx, testManTx):
   print "Starting TestMan!"
   tMan = TestMan(testManRx, testManTx)
   tMan.runProcess()

