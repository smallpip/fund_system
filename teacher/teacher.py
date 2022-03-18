# -*- coding: utf-8 -*-

import os

# from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget
from PySide2.QtCore import QDate
from PySide2.QtGui import QImageReader
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMessageBox, QAbstractItemView, QHeaderView, QTableWidgetItem, QPushButton
from pyqt5_tools.examples.exampleqmlitem import QtCore
from qt_material import apply_stylesheet
# 目录导入
import database
from database import teacher_operate, database_base, student_opreate
from lib.share import SI


# 老师窗口
class Win_tcmain:
    def __init__(self, j=None):
        # super().__init__()
        # self.ui = uic.loadUi('fund_system/main.ui',self)
        self.ui = QUiLoader().load('UI/tc_main.ui')
        self.ui.buttonChange.clicked.connect(self.onSignOut)  # 切换账号
        self.ui.button_tcchange.clicked.connect(self.on_teacher_info_change)
        self.ui.button_refresh.clicked.connect(self.reget_info)
        self.ui.tc_calendar.clicked[QDate].connect(self.showNews)

        # 个人信息
        if database_base.is_has_teacher(SI.login_username) is False:  # 如果第一次登录没有表
            sql = "INSERT INTO teacherinfo(id) VALUES('%s')" % SI.login_username
            database_base.insert(sql)
            print("已完成第一次老师建表")
        self.ui.teacher_id.setText(SI.login_username)
        a = 'name'
        SI.teacher_name = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_name.setText(SI.teacher_name)
        a = 'home'
        SI.teacher_home = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_home.setText(SI.teacher_home)
        a = 'phone'
        SI.teacher_phone = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_phone.setText(SI.teacher_phone)
        a = 'college'
        SI.teacher_college = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_college.setText(SI.teacher_college)
        a = 'email'
        SI.teacher_email = teacher_operate.teacher_op.select_teacherinfo(a, SI.login_username)
        self.ui.teacher_email.setText(SI.teacher_email)

        # 标题栏
        self.ui.label_huanyin.setText(SI.login_username)
        self.ui.label_huanyin2.setText(SI.teacher_name)

        # 公告栏
        self.ui.tc_news_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tc_news_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tc_news_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def showNews(self, date):
        self.ui.tc_news_table.clearContents()
        data = student_opreate.student_op.news_op(date.toString())
        print(data)
        self.ui.tc_news_table.setColumnCount(3)
        a = 0
        for i in data:
            a = a + 1
        self.ui.tc_news_table.setRowCount(a)
        self.ui.tc_news_table.setHorizontalHeaderLabels(['内容', '发布者','操作'])

        x = 0
        for i in data:
            y = 0
            for j in i:
                a = QTableWidgetItem(str(data[x][y]))
                self.ui.tc_news_table.setItem(x, y, a)
                y = y + 1
            lb = QPushButton('删除')
            lb.setFixedWidth(80)
            lb.setStyleSheet('QPushButton{margin:3px};')
            self.ui.tc_news_table.setCellWidget(x, y, lb)
            print(y)
            x = x + 1



    def onSignOut(self):
        SI.mainWin.ui.hide()
        SI.loginWin.ui.show()

    def on_teacher_info_change(self):
        SI.teacher_change = Win_teacher_change()
        SI.teacher_change.ui.show()

    def reget_info(self):
        self.ui.teacher_name.setText(SI.teacher_name_2)
        self.ui.teacher_home.setText(SI.teacher_home_2)
        self.ui.teacher_phone.setText(SI.teacher_phone_2)
        self.ui.teacher_id.setText(SI.teacher_id_2)
        self.ui.teacher_college.setText(SI.teacher_college_2)
        self.ui.teacher_email.setText(SI.teacher_email_2)
        self.ui.label_huanyin2.setText(SI.teacher_name_2)


# 老师信息修改
class Win_teacher_change(Win_tcmain):
    def __init__(self):
        self.ui = QUiLoader().load('UI/teacher_change.ui')
        self.ui.button_sure.clicked.connect(self.onchangeout)

    def onchangeout(self):
        SI.teacher_name_2 = self.ui.teacher_name_2.text().strip()
        SI.teacher_home_2 = self.ui.teacher_home_2.text().strip()
        SI.teacher_phone_2 = self.ui.teacher_phone_2.text().strip()
        SI.teacher_id_2 = self.ui.teacher_id_2.text().strip()
        SI.teacher_college_2 = self.ui.teacher_college_2.text().strip()
        SI.teacher_email_2 = self.ui.teacher_email_2.text().strip()

        print(SI.student_id_2)
        if not SI.teacher_id_2:
            QMessageBox.information(self.ui, 'Error', '请输入必选项', QMessageBox.Yes)
        else:
            teacher_operate.teacher_op.info_change_op(self);
            SI.teacher_change.ui.close()
