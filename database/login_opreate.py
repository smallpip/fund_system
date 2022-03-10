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
        if not SI.register_password and SI.confirm:  # 如果有一个密码或者密码确认框为空
            QMessageBox.information(self.ui, 'Error', '密码为空', QMessageBox.Yes)
        elif database_base.is_has(SI.register_username):  # 如果用户名已经存在\
            QMessageBox.information(self.ui, 'Error', '密码已经存在', QMessageBox.Yes)
        else:
            if SI.register_password == SI.confirm and SI.register_password:  # 如果两次密码一致，并且不为空
                sql = "INSERT INTO userinfo(username, password) VALUES('%s','%s')" % (
                    SI.register_username, SI.register_password)  # 添加入数据库
                database_base.insert(sql)
                QMessageBox.information(self.ui, 'Successfully', '宝，注册成功'.format(SI.register_username),
                                        QMessageBox.Yes)
            else:
                QMessageBox.information(self.ui, 'Error', '密码不相等', QMessageBox.Yes)

    def login_in(self):
        if not SI.login_password:
            QMessageBox.information(self.ui, 'Error', '密码为空', QMessageBox.Yes)
        elif database_base.is_has(SI.login_username) is None:
            QMessageBox.information(self.ui, 'Error', '用户名不存在', QMessageBox.Yes)
        else:
            sql = "select distinct password from userinfo where username='%s'" % SI.login_username
            if database_base.query(sql) != SI.login_password:
                QMessageBox.information(self.ui, 'Error', '密码不正确', QMessageBox.Yes)
            else:
                SI.login_signal = True
