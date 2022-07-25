import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtCore import QEventLoop
import py

from test import MyBot

class myBot:
  def __init__(self):
    pass
  
  def login(self):
    self.dynamicCall("ComConncect()")
    self.QEventLoop.exec()

if __name__=='__main__':
  app = QApplication(sys.argv)
  bot = myBot()
  bot.login()
  app.exec()
