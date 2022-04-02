# -*- coding: utf-8 -*-
import os
import sys

from PySide2.QtGui import QImageReader
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox
from qt_material import apply_stylesheet

from database import login_opreate
from lib.share import SI
# 登录窗口
from student import student
from teacher import teacher


class Win_Login(object):

    def __init__(self):
        # 从文件中加载UI定义
        # super().__init__()
        # self.ui = uic.loadUi('fund_system/login.ui',self)
        self.ui = QUiLoader().load('UI/login.ui')
        # 页面设置
        lable_login = self.ui.lable_login
        apply_stylesheet(lable_login, theme='light_pink.xml', extra={'font_size': 50, })
        # 功能设置
        self.ui.button_login.clicked.connect(self.onSign)  # 登录
        self.ui.button_register.clicked.connect(self.onRegister)  # 注册
        self.ui.edit_password.returnPressed.connect(lambda: self.onLogin)

    def onRegister(self):
        SI.mainWin = Win_register()
        SI.mainWin.ui.show()
        self.ui.edit_password.setText('')
        self.ui.hide()

    def onSign(self):
        # 获取界面的账户密码
        SI.login_username = self.ui.edit_username.text().strip()
        SI.login_password = self.ui.edit_password.text().strip()  # strip去除空格
        login_opreate.login_op.login_in(self)
        if SI.login_signal is True:
            comtext = self.ui.combox_login.currentText()
            if comtext == "学生":
                # 实例化一个窗口
                SI.mainWin = student.Win_Main()
                # 显示新窗口
                SI.mainWin.ui.show()
                # 清除密码
                self.ui.edit_password.setText('')
                self.ui.hide()
            else:
                SI.mainWin = teacher.Win_tcmain()
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
        SI.confirm = self.ui.confirm.text().strip()
        login_opreate.login_op.register(self)
        SI.mainWin.ui.hide()
        SI.loginWin.ui.show()


extra = {
    # Font
    'font_family': '黑体',
    'font_size': 20,
}

if __name__ == "__main__":
    # QImageReader.supportedImageFormats()
    app = QApplication(sys.argv)
    #   app.addLibraryPath(os.path.join(os.path.dirname(QtCore.__file__), "plugins"))
    SI.loginWin = Win_Login()
    # 添加样式
    apply_stylesheet(app, theme='light_pink.xml', invert_secondary=True, extra=extra)
    SI.loginWin.ui.show()
    app.exec_()
