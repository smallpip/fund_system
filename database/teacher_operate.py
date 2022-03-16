# -*- coding: utf-8 -*-
import mysql
from PySide2.QtGui import QImageReader
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow
from PySide2.QtUiTools import QUiLoader
from pyqt5_tools.examples.exampleqmlitem import QtCore
import sys

from database import database_base

from lib.share import SI


class teacher_op():
    def __init__(self):
        pass

    def select_teacherinfo(info, id):
        sql = "select %s from teacherinfo where id='%s'" % (info, id)
        return database_base.query(sql)

    def info_change_op(self):
        print("已调用")
        sql = "UPDATE teacherinfo SET name='%s',home='%s',phone='%s',college='%s',email='%s' WHERE id=%s; " % (
            SI.teacher_name_2,
            SI.teacher_home_2,
            SI.teacher_phone_2,
            SI.teacher_college_2,
            SI.teacher_email_2,
            SI.teacher_id_2)
        print(sql)
        database_base.insert(sql)
