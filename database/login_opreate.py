# -*- coding: utf-8 -*-
import mysql
from PySide2.QtGui import QImageReader
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide2.QtUiTools import QUiLoader
from pyqt5_tools.examples.exampleqmlitem import QtCore
import sys

from database import database_base

sys.path.append("../../fund system/fund_system/")  # 返回上层路径
from lib.share import SI


class login_op(object):
    def __init__(self):

        super(login_op, self).__init__()

    def register(self):
        print("调用register")
        if not SI.register_password and SI.confirm:  # 如果有一个密码或者密码确认框为空
            QMessageBox.information(self.ui,'Error', 'The password is empty', QMessageBox.Yes)
        elif database_base.is_has(SI.register_username):  # 如果用户名已经存在\
            QMessageBox.information(self.ui, 'Error', 'The username already exists', QMessageBox.Yes)
        else:
            if SI.register_password == SI.confirm and SI.register_password:  # 如果两次密码一致，并且不为空
                sql = "INSERT INTO userinfo(username, password) VALUES('%s','%s')" % (
                    SI.register_username, SI.register_password)  # 添加入数据库
                database_base.insert(sql)
                QMessageBox.information(self.ui, 'Successfully', '宝，注册成功，胜利第一步'.format(SI.register_username),
                                        QMessageBox.Yes)
                self.close()  # 注册完毕之后关闭窗口
            else:
                QMessageBox.information(self.ui, 'Error', 'The password is not equal', QMessageBox.Yes)
        print("调用register完")
