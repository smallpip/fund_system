# -*- coding: utf-8 -*-

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
        database_base.exec(sql)

    def news_op(date):
        sql = "select content,username from newsinfo where time='%s' order by id desc;" % date
        print(sql)
        return database_base.query2(sql)
