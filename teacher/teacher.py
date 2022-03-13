# -*- coding: utf-8 -*-

import os

# from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget
from PySide2.QtGui import QImageReader
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from pyqt5_tools.examples.exampleqmlitem import QtCore
from qt_material import apply_stylesheet
#目录导入
import database
from database import login_opreate
from lib.share import SI
from student import student

# 老师窗口
class Win_tcmain:
    def __init__(self, j=None):
        # super().__init__()
        # self.ui = uic.loadUi('fund_system/main.ui',self)
        self.ui = QUiLoader().load('UI/tc_main.ui')
        self.ui.buttonChange.clicked.connect(self.onSignOut)  # 切换账号

    def onSignOut(self):
        SI.mainWin.ui.hide()
        SI.loginWin.ui.show()
