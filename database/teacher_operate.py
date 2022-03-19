# -*- coding: utf-8 -*-

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
        database_base.exec(sql)

    def publish_on(self, text):
        print("publish_on已调用")
        sql = "insert into newsinfo(content, time,username) VALUES('%s','%s','%s') " % (text, SI.publish_date, SI.teacher_name)
        database_base.exec(sql)

    def publish_out(self,text):
        print('publish_out')
        sql="delete from newsinfo where content='%s' "%text
        database_base.exec(sql)

