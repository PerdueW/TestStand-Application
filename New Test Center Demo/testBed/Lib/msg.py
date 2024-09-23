#!/usr/bin/python

class Msg:
   def __init__(self, name="message",myDict = None):
      self.name = name
      if myDict is None:
         self.myDict = {}
      else:
         self.myDict = myDict.copy()
   
   def getMsgType(self):
      return self.name

   def addItem(self, name, value):
      self.myDict[name] = value

   def getItem(self, name):
      if name in self.myDict.keys():
         return self.myDict[name]
      else:
         return None

   def __str__(self):
      printStr = "MSG("+self.name+")\n"
      for key, value in self.myDict.iteritems():
         printStr += "   " + key + " : " + value + "\n"
      return printStr 

