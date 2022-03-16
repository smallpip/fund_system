# -*- coding: utf-8 -*-
import mysql
from PySide2.QtGui import QImageReader
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide2.QtUiTools import QUiLoader
from pyqt5_tools.examples.exampleqmlitem import QtCore
import sys

from database import database_base

from lib.share import SI


class student_op():
    def __init__(self):
        pass

    def select_studentinfo(info, id):
        sql = "select %s from studentinfo where id='%s'" % (info, id)
        return database_base.query(sql)

    def info_change_op(self):
        print("已调用")
        sql = "UPDATE studentinfo SET name='%s',home='%s',phone='%s',college='%s',class='%s',birth='%s',email='%s',sfzid='%s'," \
              "live='%s',identity='%s',income='%s' WHERE id=%s; " % (SI.student_username_2,
                                                               SI.student_home_2,
                                                               SI.student_phone_2,
                                                               SI.student_college_2,
                                                               SI.student_class_2,
                                                               SI.student_birth_2,
                                                               SI.student_email_2,
                                                               SI.student_sfzid_2,
                                                               SI.student_live_2,
                                                               SI.student_identity_2,
                                                               SI.student_income_2,
                                                               SI.student_id_2)
        print(sql)
        database_base.insert(sql)

    def news_op(data):
        sql="select * from news where data='%s'"%data
        return database_base.query(sql)