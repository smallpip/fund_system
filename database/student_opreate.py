# -*- coding: utf-8 -*-
from datetime import datetime

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
        database_base.exec(sql)

    def news_op(date):
        sql = "select content,username from newsinfo where time='%s' order by id desc;" % date
        return database_base.query2(sql)

    def apply_insert(self):
        print('apply已调用')
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(time)
        sql = "insert into %s(time,audit,name,fund,content,file,id,kind) VALUES('%s','未审核','%s','yes','%s','%s','%s'," \
              "'%s');" % (
                  SI.apply_fund, time, SI.student_username, SI.apply_text, SI.apply_file, SI.student_id,
                  SI.apply_kind)
        database_base.exec(sql)

    def apply_table(self, fund):
        print('fund_search已调用')
        if fund == 1:
            sql = "select time,id,name,audit,file,kind from fundinfo1 where id=%s union all select time,id,name,audit," \
                  "file,kind from " \
                  "fundinfo2 where id=%s union all select time,id,name,audit,file,kind from fundinfo3 where id='%s'" % (
                      SI.student_id, SI.student_id, SI.student_id)
            return database_base.query2(sql)
        if fund == 2:
            sql = "select time,id,name,audit,file,kind from fundinfo4 where id=%s union all select time,id,name,audit," \
                  "file,kind from " \
                  "fundinfo5 where id=%s;" % (SI.student_id, SI.student_id)
            return database_base.query2(sql)
        if fund == 3:
            sql = "select time,id,name,audit,file,kind from fundinfo6 where id=%s  ;" % (SI.student_id)
            return database_base.query2(sql)
        sql = "select time,id,name,audit,file,kind from %s where id=%s;" % (fund, SI.student_id)
        return database_base.query2(sql)

    def apply_search(self, info):
        sql = "select %s from %s where id=%s;" % (info, SI.apply_fund, SI.student_id)
        return database_base.query2(sql)

    def apply_out(self, table, id):
        print('apply_out')
        if table == '国家助学金': table = 'fundinfo1'
        if table == '国家励志奖学金': table = 'fundinfo2'
        if table == '国家助学贷款': table = 'fundinfo3'
        if table == '1号奖助金': table = 'fundinfo4'
        if table == '2号奖助金': table = 'fundinfo5'
        if table == '校内资助金': table = 'fundinfo6'
        sql = "delete from %s where id=%s " % (table.lstrip(''), id)
        database_base.exec(sql)

    def apply_change(self, table):
        print('apply_out')
        if table == '国家助学金': table = 'fundinfo1'
        if table == '国家励志奖学金': table = 'fundinfo2'
        if table == '国家助学贷款': table = 'fundinfo3'
        if table == '1号奖助金': table = 'fundinfo4'
        if table == '2号奖助金': table = 'fundinfo5'
        if table == '校内资助金': table = 'fundinfo6'
        sql = "UPDATE %s SET file='%s',content='%s' where id=%s" % (table.lstrip(''),SI.apply_file,SI.apply_text, SI.student_id)
        print(sql)
        database_base.exec(sql)


    def apply_re_search(self, table,info):
        if table == '国家助学金': table = 'fundinfo1'
        if table == '国家励志奖学金': table = 'fundinfo2'
        if table == '国家助学贷款': table = 'fundinfo3'
        if table == '1号奖助金': table = 'fundinfo4'
        if table == '2号奖助金': table = 'fundinfo5'
        if table == '校内资助金': table = 'fundinfo6'
        sql = "select %s from %s where id=%s;" % (info, table, SI.student_id)
        return database_base.query2(sql)