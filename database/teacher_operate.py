# -*- coding: utf-8 -*-
import random
from PySide2.QtWidgets import QMessageBox

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
        database_base.exec(sql)

    def publish_on(self, text):
        print("publish_on已调用")
        sql = "insert into newsinfo(content, time,username) VALUES('%s','%s','%s') " % (
            text, SI.publish_date, SI.teacher_name)
        database_base.exec(sql)

    def publish_out(self, text):
        print('publish_out')
        sql = "delete from newsinfo where content='%s' " % text
        database_base.exec(sql)

    def search(self):
        print("search已调用")
        if SI.search_id == '无':
            if SI.search_name == '无':
                if SI.search_college == '无':
                    if SI.search_class == '无':
                        QMessageBox.information(self.ui, 'Error', '请输入内容', QMessageBox.Yes)
                    else:
                        sql = "select college,class,id,name from studentinfo where class='%s'" % (
                            SI.search_class)
                        data = database_base.query2(sql)
                        return data
                else:
                    if SI.search_class == '无':
                        sql = "select college,class,id,name from studentinfo where  college='%s'" % (
                            SI.search_college)
                        data = database_base.query2(sql)
                        return data

                    else:
                        sql = "select college,class,id,name from studentinfo where class='%s' and college='%s'" % (
                            SI.search_class, SI.search_college)
                        data = database_base.query2(sql)
                        return data
            else:
                if SI.search_college == '无':
                    if SI.search_class == '无':
                        sql = "select college,class,id,name from studentinfo where name='%s'" % (
                            SI.search_name)
                        data = database_base.query2(sql)
                        return data
                    else:
                        sql = "select college,class,id,name from studentinfo where name='%s' and class='%s'" % (
                            SI.search_name, SI.search_class)
                        data = database_base.query2(sql)
                        return data

                else:
                    if SI.search_class == '无':
                        sql = "select college,class,id,name from studentinfo where name='%s' and college='%s'" % (
                            SI.search_name, SI.search_college)
                        data = database_base.query2(sql)
                        return data

                    else:
                        sql = "select college,class,id,name from studentinfo where name='%s' and class='%s' and college='%s'" % (
                            SI.search_name, SI.search_class, SI.search_college)
                        data = database_base.query2(sql)
                        return data

        else:
            if SI.search_name == '无':
                if SI.search_college == '无':
                    if SI.search_class == '无':
                        sql = "select college,class,id,name from studentinfo where id='%s' " % (
                            SI.search_id)
                        data = database_base.query2(sql)
                        return data
                    else:
                        sql = "select college,class,id,name from studentinfo where name='%s' and class='%s'" % (
                            SI.search_id, SI.search_class)
                        data = database_base.query2(sql)
                        return data
                else:
                    if SI.search_class == '无':
                        sql = "select college,class,id,name from studentinfo where id='%s' and college='%s' " % (
                            SI.search_id, SI.search_college)
                        data = database_base.query2(sql)
                        return data

                    else:
                        sql = "select college,class,id,name from studentinfo where id='%s' and class='%s' and " \
                              "college='%s'" % (
                                  SI.search_id, SI.search_class, SI.search_college)
                        data = database_base.query2(sql)
                        return data

            else:
                if SI.search_college == '无':
                    if SI.search_class == '无':
                        sql = "select college,class,id,name from studentinfo where id='%s' and name='%s' " % (
                            SI.search_id, SI.search_name)
                        data = database_base.query2(sql)
                        return data

                    else:
                        sql = "select college,class,id,name from studentinfo where id='%s' and name='%s' and class='%s'" % (
                            SI.search_id, SI.search_name, SI.search_class)
                        data = database_base.query2(sql)
                        return data
                else:
                    sql = "select college,class,id,name from studentinfo where id='%s' and name='%s' and class='%s' " \
                          "and college='%s'" % (
                              SI.search_id, SI.search_name, SI.search_class, SI.search_college)
                    data = database_base.query2(sql)
                    return data

    # 贫困生搜索
    def search_detail(self):
        print('search_detail已调用')
        sql = "select * from studentinfo where id='%s'" % SI.text
        data = database_base.query2(sql)
        search_value(self, data)

    # 资助搜索
    def fund_search(self, table):
        print('fund_search已调用')
        sql = "select time,id,name,audit,file from %s where fund='yes';" % (table)
        return database_base.query2(sql)

    def check_reject(self, table, info):
        sql = "UPDATE %s SET audit='驳回' WHERE id='%s';" % (table, info)
        database_base.exec(sql)
        sql = "UPDATE studentinfo SET renzhen='已认证' WHERE id=%s;" % info
        database_base.exec(sql)

    def check_pass(self, table, info):
        sql = "UPDATE %s SET audit='已审核' WHERE id='%s';" % (table, info)
        database_base.exec(sql)
        sql = "UPDATE studentinfo SET renzhen='已认证' WHERE id=%s;" % info
        database_base.exec(sql)

    #贫困认定搜索
    def pinkun_search(self):
        print('fund_search已调用')
        sql = "select time,id,name,identity from pinkuninfo ;"
        return database_base.query2(sql)

    def pinkun_reject(self, info):
        print('check已调用')
        sql = "UPDATE pinkuninfo SET identity='驳回' WHERE id='%s';" % info
        database_base.exec(sql)
        sql = "UPDATE studentinfo SET renzhen='驳回' WHERE id=%s;" % info
        database_base.exec(sql)

    def pinkun_pass(self, info):
        print('check已调用')
        sql = "UPDATE pinkuninfo SET identity='已认证' WHERE id='%s';" % info
        database_base.exec(sql)
        sql = "UPDATE studentinfo SET renzhen='已认证' WHERE id=%s;" % info
        database_base.exec(sql)
   #绘图数据
    def tu_kind_college(self):
        sql="select distinct college from studentinfo where renzhen='已认证';"
        data=database_base.query2(sql)
        return list(data)

    def tu_count_college(self):
        sql = "select distinct college from studentinfo where renzhen='已认证';"
        data = database_base.query2(sql)
        data1=[]
        for i in range(len(data)):
            sql="select sum(college='%s') from studentinfo where renzhen='已认证';"%data[i][0]
            data1.append(int(database_base.query(sql)))
        data1 = list(map(int, data1))
        return data1

    def tu2_count(self):
        sql = "select sum(renzhen='已认证') from studentinfo ;"
        data = database_base.query(sql)
        return data

    def tu3_count(self):
        sql = "select sum(zizhu='已资助') from studentinfo ;"
        data = database_base.query(sql)
        return data

    def tu4_count(self):
        sql = "select college,sum(renzhen='已认证') from studentinfo group by college; "
        data = database_base.query2(sql)
        return data

def search_value(self, data):
    SI.search_name = data[0][0]
    SI.search_home = data[0][1]
    SI.search_phone = data[0][2]
    SI.search_college = data[0][3]
    SI.search_class = data[0][4]
    SI.search_id = data[0][5]
    SI.search_birth = data[0][6]
    SI.search_email = data[0][7]
    SI.search_sfzid = data[0][8]
    SI.search_live = data[0][9]
    SI.search_identity = data[0][10]
    SI.search_income = data[0][11]
    SI.search_pinkun = data[0][12]
    SI.search_hukou = data[0][13]
    print("search_value")
    print(SI.search_name)
#颜色随机
def randomcolor(i):
    colorArr = ['#fbffcf','#cfffeb','#d3cfff','#cfe3ff','#e3ffcf','#ffd3cf','#6a4dff']
    color = colorArr[i]
    return color