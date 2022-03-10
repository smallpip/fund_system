# -*- coding: utf-8 -*-

import os

# from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget
from PySide2.QtGui import QImageReader
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from pyqt5_tools.examples.exampleqmlitem import QtCore
from qt_material import apply_stylesheet

import database
from database import login_opreate
from lib.share import SI


class Win_Login(object):

    def __init__(self):
        # 从文件中加载UI定义
        # super().__init__()
        # self.ui = uic.loadUi('fund_system/login.ui',self)
        self.ui = QUiLoader().load('UI/login.ui')
        self.ui.button_login.clicked.connect(self.onSign)#登录
        self.ui.button_register.clicked.connect(self.onRegister)#注册
        self.ui.edit_password.returnPressed.connect(lambda: self.onLogin)

    def onRegister(self):
        SI.mainWin = Win_register()
        SI.mainWin.ui.show()
        self.ui.edit_password.setText('')
        self.ui.hide()

    def onSign(self):
        # 获取界面的账户密码
        username = self.ui.edit_username.text().strip()
        password = self.ui.edit_password.text().strip()  # strip去除空格
        comtext = self.ui.combox_login.currentText()
        if comtext == "学生":
            # 实例化一个窗口
            SI.mainWin = Win_Main()
            # 显示新窗口
            SI.mainWin.ui.show()
            # 清除密码
            self.ui.edit_password.setText('')
            self.ui.hide()
        else:
            SI.mainWin = Win_tcmain()
            # 显示新窗口
            SI.mainWin.ui.show()
            # 清除密码
            self.ui.edit_password.setText('')
            self.ui.hide()


# 注册窗口
class Win_register():
    def __init__(self):
        self.ui = QUiLoader().load('UI/register.ui')
        self.ui.button_determine.clicked.connect(self.onRegisterout)

    def onRegisterout(self):
        SI.register_username = self.ui.register_username.text().strip()
        SI.register_password = self.ui.register_password.text().strip()
        SI.confirm=self.ui.confirm.text().strip()
        login_opreate.login_op.register(self)
        SI.mainWin.ui.hide()
        SI.loginWin.ui.show()

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


# 学生窗口
class Win_Main:
    def __init__(self, j=None):
        # super().__init__()
        # self.ui = uic.loadUi('fund_system/main.ui',self)
        self.ui = QUiLoader().load('UI/main.ui')
        self.ui.buttonChange.clicked.connect(self.onSignOut)  # 切换账号

    def onSignOut(self):
        SI.mainWin.ui.hide()
        SI.loginWin.ui.show()





QImageReader.supportedImageFormats()
app = QApplication([])
app.addLibraryPath(os.path.join(os.path.dirname(QtCore.__file__), "plugins"))
SI.loginWin = Win_Login()
# 添加样式
apply_stylesheet(app, theme='light_pink.xml', invert_secondary=True)
SI.loginWin.ui.show()
app.exec_()
