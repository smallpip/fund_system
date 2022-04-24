# -*- coding: utf-8 -*-
from datetime import datetime

from PySide2.QtWidgets import QMessageBox

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

    def pinkun_table(self):
        sql="select time,id,name,identity from pinkuninfo where id=%s;" % SI.student_id
        return database_base.query2(sql)

    def pinkun_insert(self):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into pinkuninfo(time,name,identity,content,file,id) VALUES('%s','%s','未认定','%s','%s'," \
              "'%s');" % (
                   time, SI.student_username, SI.apply_text, SI.apply_file, SI.student_id)
        database_base.exec(sql)

    def pinkun_table_op(self,info):
        sql = "select %s from pinkuninfo where id=%s;" % (info,SI.student_id)
        return database_base.query2(sql)

    def pinkun_change(self):
        sql = "UPDATE pinkuninfo SET file='%s',content='%s' where id=%s" % (SI.apply_file,SI.apply_text, SI.student_id)
        database_base.exec(sql)

    def pinkun_out(self, id):
        sql = "delete from pinkuninfo where id=%s " % id
        database_base.exec(sql)

    def apply_pinkun(self):
        sql = "select identity from pinkuninfo where id=%s " % SI.student_id
        data=database_base.query(sql)
        print(data)
        if data=='已认证':
            return True
        else:
            return False

    def job_apply(self,id,work_name,username,place,salary,connect,end,work_t):
        if database_base.is_h(d_name='id',info='%s'%SI.student_id,table='job_application')is False:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql="insert into job_application(id,work_name,time,username,state,place,salary,connect,end,work_t) VALUES('%s','%s','%s','%s','已申请','%s','%s','%s','%s','%s')"% (id,work_name,time,username,place,salary,connect,end,work_t)
            print(sql)
            database_base.exec(sql)

        else:
            QMessageBox.information(self.ui, 'Error', '已申请', QMessageBox.Yes)

    def job_search(self):
        sql = "select work_name,place,work_t,connect,salary,end from job_application where id=%s"%SI.id
        print(sql)
        return database_base.query2(sql)

    def job_del(self, id):
        sql = "delete from job_application where id=%s " % id
        database_base.exec(sql)
