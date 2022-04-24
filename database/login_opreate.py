# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QMessageBox

from database import database_base
from lib.share import SI


class login_op(object):
    def __init__(self):

        super(login_op, self).__init__()

    def register(self):
        if not SI.register_password and SI.confirm:  # 如果有一个密码或者密码确认框为空
            QMessageBox.information(self.ui, 'Error', '密码为空', QMessageBox.Yes)
        elif database_base.is_has(SI.register_username):  # 如果用户名已经存在\
            QMessageBox.information(self.ui, 'Error', '用户已经存在', QMessageBox.Yes)
        else:
            if SI.register_password == SI.confirm and SI.register_password:  # 如果两次密码一致，并且不为空
                if 0 <= int(SI.register_username) <= 999:
                    sql = "INSERT INTO studentinfo(id,name,home,phone,college,class,birth,email,sfzid,live,identity," \
                          "income,pinkun,hukou,renzhen,zizhu) VALUES('%s','无','无','无','计科','无','无','无','无','无','无'," \
                          "'无','无','无','无','无')" % SI.register_username
                    database_base.exec(sql)
                    sql = "INSERT INTO userinfo(username, password,sf) VALUES('%s','%s','学生')" % (
                        SI.register_username, SI.register_password)  # 添加入数据库
                    database_base.exec(sql)
                if 1000 <= int(SI.register_username)  <= 1999:
                    sql = "INSERT INTO studentinfo(id,name,home,phone,college,class,birth,email,sfzid,live,identity," \
                          "income,pinkun,hukou,renzhen,zizhu) VALUES('%s','无','无','无','物电','无','无','无','无','无','无'," \
                          "'无','无','无','无','无')" % SI.register_username
                    database_base.exec(sql)
                    sql = "INSERT INTO userinfo(username, password,sf) VALUES('%s','%s','学生')" % (
                        SI.register_username, SI.register_password)  # 添加入数据库
                    database_base.exec(sql)
                if 2000 <= int(SI.register_username)  <= 2999:
                    sql = "INSERT INTO studentinfo(id,name,home,phone,college,class,birth,email,sfzid,live,identity," \
                          "income,pinkun,hukou,renzhen,zizhu) VALUES('%s','无','无','无','数科','无','无','无','无','无','无'," \
                          "'无','无','无','无','无')" % SI.register_username
                    database_base.exec(sql)
                    sql = "INSERT INTO userinfo(username, password,sf) VALUES('%s','%s','学生')" % (
                        SI.register_username, SI.register_password)  # 添加入数据库
                    database_base.exec(sql)
                if 3000 <= int(SI.register_username)  <= 3999:
                    sql = "INSERT INTO studentinfo(id,name,home,phone,college,class,birth,email,sfzid,live,identity," \
                          "income,pinkun,hukou,renzhen,zizhu) VALUES('%s','无','无','无','化院','无','无','无','无','无','无'," \
                          "'无','无','无','无','无')" % SI.register_username
                    database_base.exec(sql)
                    sql = "INSERT INTO userinfo(username, password,sf) VALUES('%s','%s','学生')" % (
                        SI.register_username, SI.register_password)  # 添加入数据库
                    database_base.exec(sql)
                if 4000 <= int(SI.register_username)  <= 4999:
                    sql = "INSERT INTO teacherinfo(id,name,home,phone,college,email) VALUES('%s','无','无','无','计科','无')" % SI.login_username
                    database_base.exec(sql)
                    sql = "INSERT INTO userinfo(username, password,sf) VALUES('%s','%s','老师')" % (
                        SI.register_username, SI.register_password)  # 添加入数据库
                    database_base.exec(sql)
                if 4000 <= int(SI.register_username)  <= 4999:
                    sql = "INSERT INTO teacherinfo(id,name,home,phone,college,email) VALUES('%s','无','无','无','物电','无')" % SI.login_username
                    database_base.exec(sql)
                    sql = "INSERT INTO userinfo(username, password,sf) VALUES('%s','%s','老师')" % (
                        SI.register_username, SI.register_password)  # 添加入数据库
                    database_base.exec(sql)
                if 5000 <= int(SI.register_username)  <= 5999:
                    sql = "INSERT INTO teacherinfo(id,name,home,phone,college,email) VALUES('%s','无','无','无','数科','无')" % SI.login_username
                    database_base.exec(sql)
                    sql = "INSERT INTO userinfo(username, password,sf) VALUES('%s','%s','老师')" % (
                        SI.register_username, SI.register_password)  # 添加入数据库
                    database_base.exec(sql)
                if 6000 <= int(SI.register_username)  <= 6999:
                    sql = "INSERT INTO teacherinfo(id,name,home,phone,college,email) VALUES('%s','无','无','无','化院','无')" % SI.login_username
                    database_base.exec(sql)
                    sql = "INSERT INTO userinfo(username, password,sf) VALUES('%s','%s','老师')" % (
                        SI.register_username, SI.register_password)  # 添加入数据库
                    database_base.exec(sql)
                QMessageBox.information(self.ui, 'Successfully', '宝，注册成功'.format(SI.register_username),
                                        QMessageBox.Yes)
            else:
                QMessageBox.information(self.ui, 'Error', '密码不相等', QMessageBox.Yes)

    def login_in(self):
        print(database_base.is_has(SI.login_username))
        if not SI.login_password:
            QMessageBox.information(self.ui, 'Error', '密码为空', QMessageBox.Yes)
        elif database_base.is_has(SI.login_username) is False:
            QMessageBox.information(self.ui, 'Error', '用户名不存在', QMessageBox.Yes)
        else:
            sql = "select distinct password from userinfo where username='%s'" % SI.login_username
            if database_base.query(sql) != SI.login_password:
                QMessageBox.information(self.ui, 'Error', '密码不正确', QMessageBox.Yes)
            else:
                SI.login_signal = True

    def login_match(self):
        sql= "select distinct sf from userinfo where username='%s'" % SI.login_username
        return database_base.query(sql)