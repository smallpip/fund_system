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


class student_op():
    def __init__(self):
        pass

    def select_studentinfo(info, id):
        sql = "select '%s' from studentinfo where id='%s'" % (info, id)
        return database_base.query(sql)

    def info_change_op(self):
        sql = "INSERT INTO studentinfo(name,home,phone,college,class,id,birth,email,sfzid,live,identity,income) VALUES(" \
              "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (SI.student_username_2,
                                                                                     SI.student_home_2,
                                                                                     SI.student_phone_2,
                                                                                     SI.student_college_2,
                                                                                     SI.student_class_2,
                                                                                     SI.student_id_2,
                                                                                     SI.student_birth_2,
                                                                                     SI.student_email_2,
                                                                                     SI.student_sfzid_2,
                                                                                     SI.student_live_2,
                                                                                     SI.student_identity_2,
                                                                                     SI.student_income_2)
        database_base.insert(sql)
