# -*- coding: utf-8 -*-
# opc.tcp://203.239.91.196:51235
# ns=12;i=29576

import sys
import uihelper
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = uihelper.MyApp()
   sys.exit(app.exec_())
