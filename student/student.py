# -*- coding: utf-8 -*-

import os

# from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget
from PySide2.QtGui import QImageReader
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox
from pyqt5_tools.examples.exampleqmlitem import QtCore
from qt_material import apply_stylesheet
# 目录导入
from database import database_base
from database import login_opreate
from lib.share import SI
from teacher import teacher
from database import student_opreate


# 学生窗口
class Win_Main:
    def __init__(self, j=None):
        # super().__init__()
        # self.ui = uic.loadUi('fund_system/main.ui',self)
        self.ui = QUiLoader().load('UI/main.ui')
        self.ui.buttonChange.clicked.connect(self.onSignOut)  # 切换账号
        self.ui.info_change.clicked.connect(self.on_student_info_change)

        # 个人信息
        if database_base.is_has_student(SI.login_username) is False:  # 如果第一次登录没有表
            sql = "INSERT INTO studentinfo(id) VALUES('%s')" % SI.login_username
            database_base.insert(sql)

        #个人信息获取
        self.ui.student_id.settext(SI.login_username)

        a = 'username'
        SI.student_username = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_username.settext(SI.student_username)
        a = 'home'
        SI.student_home = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_home.settext(SI.student_home)
        a = 'phone'
        SI.student_phone = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_phone.settext(SI.student_home)
        a = 'college'
        SI.student_college = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_college.settext(SI.student_college)
        a = 'class'
        SI.student_class = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_class.settext(SI.student_class)
        a = 'email'
        SI.student_email = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_email.settext(SI.student_email)
        a = 'sfzid'
        SI.student_sfzid = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_sfzid.settext(SI.student_sfzid)
        a = 'live'
        SI.student_live = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_live.settext(SI.student_live)
        a = 'dentity'
        SI.student_identity = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_identity.settext(SI.student_identity)
        a = 'income'
        SI.student_income = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_income.settext(SI.student_income)
        a = 'pinkun'
        SI.student_pinkun = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_pinkun.currentText(SI.student_pinkun)
        a = 'hukou'
        SI.student_hukou = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_hukou.currentText(SI.student_hukou)
        a = 'birth'
        SI.student_birth = student_opreate.student_op.select_studentinfo(a, SI.login_username)
        self.ui.student_birth.settext(SI.student_birth)

    def on_student_info_change(self):
        super(Win_Main, self).on_student_info_change()
        SI.student_change = Win_student_change()
        SI.student_change.ui.show()

    def onSignOut(self):
        SI.mainWin.ui.hide()
        SI.loginWin.ui.show()


class Win_student_change():
    def __init__(self):
        self.ui = QUiLoader().load('../UI/student_change.ui')
        self.ui.butto_sure.clicked.connect(self.onchangeout)
        SI.student_username_2 = self.ui.student_username_2.text().strip()
        SI.student_home_2 = self.ui.student_home_2.text().strip()
        SI.student_phone_2 = self.ui.student_phone_2.text().strip()
        SI.student_college_2 = self.ui.student_college_2.text().strip()
        SI.student_class_2 = self.ui.student_class_2.text().strip()
        SI.student_id_2 = self.ui.student_id_2.text().strip()
        SI.student_email_2 = self.ui.student_email_2.text().strip()
        SI.student_sfzid_2 = self.ui.student_sfzid_2.text().strip()
        SI.student_live_2 = self.ui.student_live_2.text().strip()
        SI.student_birth_2=self.ui.student_birth_2.text().strip()
        SI.student_identity_2 = self.ui.student_identity_2.text().strip()
        SI.student_income_2 = self.ui.student_income_2.text().strip()
        SI.student_pinkung_2 = self.ui.comboBox_pinkun_2.currentText()
        SI.student_hukou_2 = self.ui.comboBox_hukou_2.currentText()

    def onchangeout(self):
        if not SI.student_id_2:
            QMessageBox.information(self.ui, 'Error', '请输入必选项', QMessageBox.Yes)
        else:
            student_opreate.info_change_op();
            SI.student_change.ui.close()
